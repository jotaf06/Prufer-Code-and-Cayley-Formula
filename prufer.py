def prufer_code(tree):
    vertices = len(tree) + 1
    degree = [0] * vertices

    # Contar o grau de cada vértice
    for u, v in tree:
        degree[u - 1] += 1
        degree[v - 1] += 1

    prufer_code = []
    
    # Encontre o menor nó folha (grau 1) para começar
    for _ in range(vertices - 2):
        leaf = min(i + 1 for i in range(vertices) if degree[i] == 1)
        
        # Encontre o vizinho da folha
        for u, v in tree:
            if u == leaf or v == leaf:
                neighbor = v if u == leaf else u
                break

        prufer_code.append(neighbor)
        
        # Remova a folha da árvore
        degree[leaf - 1] -= 1
        degree[neighbor - 1] -= 1

        # Remova a aresta correspondente da árvore
        tree = [(u, v) for u, v in tree if u != leaf and v != leaf]

    return prufer_code

# Exemplo de árvore (lista de arestas)
tree = [(1, 2), (1, 3), (1, 6), (2, 5), (2, 4)]

# Gerar o código de Prüfer da árvore
code = prufer_code(tree)
print("Código de Prüfer:", code)
