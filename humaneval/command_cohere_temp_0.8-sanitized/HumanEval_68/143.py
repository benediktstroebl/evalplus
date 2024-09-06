def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if even_nodes:
        smallest_even = min(even_nodes)
        min_index = even_nodes.index(smallest_even)
        return [smallest_even, min_index]
    else:
        return []