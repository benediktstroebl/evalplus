from collections import Counter
def pluck(arr):
    even_nodes = [n for n in arr if n % 2 == 0]
    if not even_nodes:
        return []

    # Use Counter to find the minimum even node and its index
    min_node, min_index = min(Counter(even_nodes).items(), key=lambda x: x[1])
    
    return [min_node, min_index]