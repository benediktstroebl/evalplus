def pluck(arr):
    # Filter even values and get the minimum node
    even_nodes = filter(lambda x: x % 2 == 0, arr)
    min_even_node = min(even_nodes, key=lambda x: (x, arr.index(x)))
    
    # Return the result as a list
    return [min_even_node, arr.index(min_even_node)]