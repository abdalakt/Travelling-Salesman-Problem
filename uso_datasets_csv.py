"""
Script para usar os arquivos CSV como datasets no projeto TSP
Versão com Python puro (sem dependências externas)
"""

import csv
from time import time
from itertools import permutations

# ================================
# FUNÇÕES PRINCIPAIS (versão Python puro)
# ================================

def read_csv_to_matrix(csv_file):
    """Converte arquivo CSV para matriz de distâncias"""
    matrix = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Pula primeira linha (cabeçalho)
        for row in reader:
            # Pula primeira coluna (nomes de cidades) e converte restante para int
            matrix.append([int(x) for x in row[1:]])
    return matrix

def calculate_path_cost(matrix, path):
    """Calcula o custo total do caminho"""
    tsp_cost = 0
    for index in range(len(path) - 1):
        line = path[index]
        column = path[index + 1]
        tsp_cost += matrix[line][column]
    return tsp_cost

def brute_force_tsp(matrix):
    """
    Força bruta para encontrar melhor caminho
    Testa todas as permutações de nós
    """
    n = len(matrix)
    if n <= 1:
        return 0, list(range(n)) + [0]
    
    nodes = list(range(1, n))  # Todos exceto o primeiro
    best_cost = float('inf')
    best_path = None
    
    count = 0
    total = 1
    for i in range(1, n):
        total *= i
    
    print(f"   Testando {total} permutações possíveis...")
    
    for perm in permutations(nodes):
        path = [0] + list(perm) + [0]
        cost = calculate_path_cost(matrix, path)
        
        if cost < best_cost:
            best_cost = cost
            best_path = path
        
        count += 1
        if count % max(1, total // 10) == 0:
            print(f"   Progresso: {count}/{total} ({100*count//total}%)")
    
    return best_cost, best_path

def approximate_tsp_simple(matrix, initial_node=0):
    """
    Algoritmo aproximativo simples - Vizinho Mais Próximo
    Começa em um nó e sempre vai para o vizinho não visitado mais próximo
    """
    n = len(matrix)
    unvisited = set(range(n))
    
    current_node = initial_node
    path = [current_node]
    unvisited.remove(current_node)
    
    # Greedy: sempre vai para o mais próximo
    while unvisited:
        nearest = min(unvisited, key=lambda node: matrix[current_node][node])
        path.append(nearest)
        unvisited.remove(nearest)
        current_node = nearest
    
    # Retorna ao nó inicial
    path.append(initial_node)
    cost = calculate_path_cost(matrix, path)
    
    return cost, path

# ================================
# ANÁLISE COM DATASETS
# ================================

def analyze_dataset(csv_file, name, use_brute_force=False):
    print(f"\n{'='*70}")
    print(f"📊 Analisando: {name}")
    print(f"   Arquivo: {csv_file}")
    print(f"{'='*70}\n")
    
    # Carregar matriz
    matrix = read_csv_to_matrix(csv_file)
    n_nodes = len(matrix)
    print(f"✓ Número de cidades: {n_nodes}")
    print(f"✓ Arquivo carregado com sucesso!\n")
    
    # Mostrar matriz se for pequena
    if n_nodes <= 10:
        print("📋 Matriz de Distâncias:")
        for i, row in enumerate(matrix):
            print(f"   Cidade {i}: {row}")
        print()
    
    # Algoritmo Aproximativo (Vizinho Mais Próximo)
    print("🔍 Executando Algoritmo Aproximativo (Vizinho Mais Próximo)...")
    costs = {}
    
    for initial_node in range(n_nodes):
        start_time = time()
        cost, path = approximate_tsp_simple(matrix, initial_node=initial_node)
        exec_time = time() - start_time
        costs[cost] = {"path": path, "time": exec_time, "initial": initial_node}
        print(f"   Nó inicial {initial_node}: Custo = {cost:6d}, Tempo = {exec_time:.6f}s")
    
    best_cost = min(costs.keys())
    best_solution = costs[best_cost]
    print(f"\n✅ MELHOR RESULTADO (Aproximativo):")
    print(f"   Custo total: {best_cost}")
    print(f"   Nó inicial: {best_solution['initial']}")
    print(f"   Caminho: {' → '.join(map(str, best_solution['path']))}")
    print(f"   Tempo: {best_solution['time']:.6f}s\n")
    
    # Força Bruta (apenas para datasets pequenos)
    if use_brute_force and n_nodes <= 10:
        print("⚠️  Executando Força Bruta (encontra solução ÓTIMA)...")
        print("   ⏳ Isso pode demorar dependendo do tamanho do dataset...\n")
        
        start_time = time()
        bf_cost, bf_path = brute_force_tsp(matrix)
        bf_time = time() - start_time
        
        print(f"\n✅ MELHOR RESULTADO (Força Bruta):")
        print(f"   Custo total: {bf_cost}")
        print(f"   Caminho: {' → '.join(map(str, bf_path))}")
        print(f"   Tempo: {bf_time:.6f}s\n")
        
        ratio = best_cost / bf_cost
        print(f"📈 ANÁLISE COMPARATIVA:")
        print(f"   Custo Aproximativo / Custo Ótimo: {ratio:.3f}x")
        print(f"   (Teoricamente ≤ 2.0x para algoritmos 2-aproximados)\n")
        
        if ratio <= 2.0:
            print(f"   ✓ VALIDADO: Resultado dentro do limite teórico!\n")
        else:
            print(f"   ⚠️  AVISO: Resultado acima do limite teórico!\n")
    
    return best_solution, matrix

# ================================
# EXECUÇÃO PRINCIPAL
# ================================

if __name__ == "__main__":
    results = {}
    
    print("\n" + "🚀 " * 25)
    print("ANÁLISE DO PROBLEMA DO CAIXEIRO VIAJANTE (TSP)")
    print("Comparação de Algoritmos em Diferentes Datasets")
    print("🚀 " * 25 + "\n")
    
    # Analisar cidades.csv
    try:
        sol1, matrix1 = analyze_dataset(
            "cidades.csv",
            "DATASET 1 - Cidades",
            use_brute_force=True
        )
        results["cidades.csv"] = (sol1, matrix1)
    except FileNotFoundError:
        print("❌ Erro: arquivo cidades.csv não encontrado!")
    
    # Analisar cidades2.csv
    try:
        sol2, matrix2 = analyze_dataset(
            "cidades2.csv",
            "DATASET 2 - Cidades 2",
            use_brute_force=True
        )
        results["cidades2.csv"] = (sol2, matrix2)
    except FileNotFoundError:
        print("❌ Erro: arquivo cidades2.csv não encontrado!")
    
    print("\n" + "="*70)
    print("✅ ANÁLISE COMPLETA!")
    print("="*70 + "\n")
    
    print("\n💡 PRÓXIMOS PASSOS:")
    print("   1. Execute o notebook travelling_salesman.ipynb para visualizações gráficas")
    print("   2. Teste com os arquivos tsp_data/*.txt para datasets maiores")
    print("   3. Compare os tempos de execução entre os algoritmos")
    print()
