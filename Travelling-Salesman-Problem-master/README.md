# Problema do Caixeiro Viajante (Travelling Salesman Problem)

## 📋 Descrição

Este projeto implementa e compara diferentes abordagens para resolver o **Problema do Caixeiro Viajante (PCV)**, um dos problemas mais famosos da Ciência da Computação. O objetivo é encontrar o caminho mais curto que percorra um conjunto de cidades exatamente uma vez e retorne à cidade inicial.

O PCV é um problema **NP-Difícil**, o que significa que não existe algoritmo conhecido que o resolva em tempo polinomial para casos gerais.

O trabalho foi desenvolvido como atividade avaliativa da disciplina **Análise de Algoritmos**, no âmbito do Mestrado em Computação Aplicada da Universidade do Vale do Itajaí (UNIVALI), no período letivo 2026/01.

## Autores

- Katia Lorenz  
- Letícia Zorzi Rama  
- Ricardo Arruda Júnior

## Orientação

Prof. Dr. Rudimar Luís Scaranto Dazzi

## 🎯 Objetivos

- Implementar uma solução por **força bruta** (garante solução ótima)
- Implementar uma solução por uma heurística qualquer. Utilizamos **algoritmo aproximativo** com Árvore Geradora Mínima
- Comparar a complexidade teórica e prática dos algoritmos
- Analisar o desempenho em diferentes tamanhos de entrada
- Demonstrar o trade-off entre qualidade da solução e tempo de execução

## 🔍 Algoritmos Implementados

### 1. Força Bruta - O(n!)
- **Estratégia**: Verifica exaustivamente todos os caminhos possíveis
- **Garantia**: Encontra sempre a melhor solução
- **Desvantagem**: Complexidade exponencial torna inviável com muitas cidades (n > 11)
- **Implementação**: Algoritmo recursivo backtracking

```
Permutações verificadas para n cidades: (n-1)!/2
```

### 2. Algoritmo Aproximativo - O(n²)
- **Estratégia**: Constrói uma Árvore Geradora Mínima (MST) e cria um ciclo hamiltoniano
- **Garantia**: Solução no máximo 2 vezes pior que o ótimo (2-aproximado)
- **Vantagem**: Complexidade polinomial permite resolver instâncias maiores
- **Implementação**: Utiliza AGM + percurso em profundidade

```
Etapas:
1. Gerar Árvore Geradora Mínima (AGM) - O(n²)
2. Fazer busca em profundidade (DFS) na AGM para criar ciclo hamiltoniano - O(n)
3. Calcular custo do caminho - O(n)
```

## Estrutura do Projeto

```
├── travelling_salesman.ipynb  # Notebook principal com análises
├── README.md                   # Este arquivo
├── requirements.txt            # Dependências do projeto
├── tsp_data/                   # Datasets com matrizes de distâncias
│   ├── capitais5.csv          # 5 capitais (pequeno)
│   ├── capitais9.csv          # 9 capitais
│   ├── capitais10.csv         # 10 capitais
│   ├── capitais11.csv         # 11 capitais
│   ├── capitais12.csv         # 12 capitais
│   ├── capitais13.csv         # 13 capitais
│   ├── capitais14.csv         # 14 capitais
│   ├── capitais_completo.csv  # 26 capitais
│   ├── cidades.csv            # Dataset adicional
│   └── cidades2.csv           # Dataset adicional
└── figures/                    # Gráficos e visualizações
```

## Como Usar

### Pré-requisitos
- Python 3.7+
- Jupyter Notebook

### Instalação

```bash
pip install -r requirements.txt
```

### Executar

```bash
jupyter notebook travelling_salesman.ipynb
```

## 📈 Análise Teórica de Complexidade

| Algoritmo | Complexidade | Máx. de Cidades | Tempo Aprox. (n=10) |
|-----------|-------------|-----------------|-------------------|
| Força Bruta | O(n!) | ~12 | Segundos |
| Aproximativo | O(n²) | sem limite | Milissegundos |

**Exemplo com n=10 cidades:**
- Força Bruta: 9! = 362.880 permutações
- Aproximativo: 10² = 100 operações

## Conteúdo do Notebook

1. **Importações e Instalação de Dependências**
   - Instala `scipy` para operações com matrizes esparsas

2. **Definição de Funções Auxiliares**
   - `read_csv_to_matrix()`: Lê matrizes de distâncias de arquivos CSV
   - `calculate_path_cost()`: Calcula o custo total de um caminho

3. **Algoritmo de Força Bruta**
   - Implementação recursiva com backtracking
   - Testa todas as permutações de caminhos possíveis

4. **Algoritmo Aproximativo**
   - Gera Árvore Geradora Mínima usando SciPy
   - Realiza DFS para construir o ciclo hamiltoniano

5. **Carregamento e Análise de Datasets**
   - Carrega múltiplos datasets com diferentes tamanhos
   - Exibe análise teórica de complexidade

6. **Execução Comparativa**
   - Executa ambos os algoritmos
   - Compara tempo de execução e qualidade da solução
   - Exibe métricas de desempenho

7. **Visualização de Resultados**
   - Gráficos comparativos (se disponíveis na pasta `figures/`)

## Formato dos Dados

Os arquivos CSV utilizam a seguinte estrutura:

```
;Cidade1;Cidade2;Cidade3;...
Cidade1;0;distância;distância;...
Cidade2;distância;0;distância;...
Cidade3;distância;distância;0;...
...
```

- Separador: `;` (ponto-e-vírgula)
- Decimal: `.` (ponto) ou `,` (vírgula)
- Matriz simétrica de distâncias
- Diagonal principal com zeros

## Insights e Conclusões

### Trade-offs
- **Força Bruta**: Exato mas exponencial
- **Aproximativo**: Rápido mas pode estar 2x acima do ótimo

### Quando Usar Cada Um
- **Força Bruta**: Problema pequeno (n ≤ 13) onde precisamos da solução exata
- **Aproximativo**: Problema grande onde velocidade é crítica

### Aplicações Práticas
- Logística e roteamento de entrega
- Planejamento de circuitos integrados
- Sequenciamento de genoma
- Otimização de rotas de turismo

## Dependências

- `scipy`: Para operações com matrizes e MST
- `numpy`: Para operações numéricas (instalado com scipy)
- `jupyter`: Para executar o notebook
- `python`: versão 3.7+
