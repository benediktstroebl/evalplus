def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if not even_nodes:
        return []

    smallest_even = min(even_nodes)
    min_index = even_nodes.index(smallest_even)
    
    return [smallest_even, min_index]