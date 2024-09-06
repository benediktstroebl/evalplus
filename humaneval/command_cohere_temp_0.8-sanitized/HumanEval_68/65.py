from collections import *
def pluck(arr):
    # Your code here!
    even_nodes = [n for n in arr if n % 2 == 0]
    if even_nodes:
        min_even_node = min(even_nodes)
        min_index = even_nodes.index(min_even_node)
        return [min_even_node, min_index]
    else:
        return []