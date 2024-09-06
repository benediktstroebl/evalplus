def pluck(arr):
    even_nodes = {node: index for index, node in enumerate(arr) if node % 2 == 0}
    if not even_nodes:
        return []
    min_value, min_index = min(even_nodes.items()), min(even_nodes, key=even_nodes.get)
    return [min_value, min_index]