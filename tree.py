import networkx as nx
import matplotlib.pyplot as plt

# Função para converter um código de Prüfer para uma árvore
def prufer_to_tree(prufer_code):
    vertices = len(prufer_code) + 2
    degree = [1] * vertices

    # Ajustar os graus de acordo com o código de Prüfer
    for node in prufer_code:
        degree[node - 1] += 1

    tree = []
    for node in prufer_code:
        for i in range(vertices):
            if degree[i] == 1:
                tree.append((i + 1, node))  # Usar (i + 1) para ajustar à indexação
                degree[i] -= 1
                degree[node - 1] -= 1
                break

    # Adicionar a última aresta
    u, v = [i + 1 for i in range(vertices) if degree[i] == 1]
    tree.append((u, v))

    return tree

# Exemplo de código de Prüfer
prufer_code = [1, 2, 2, 1]

# Converta o código de Prüfer para uma árvore
edges = prufer_to_tree(prufer_code)

# Crie um grafo e adicione as arestas
G = nx.Graph()
G.add_edges_from(edges)

# Desenhe e exiba a árvore
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()
