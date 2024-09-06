from collections import Counter
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    smallest_even, index = min(even_nodes), even_nodes.index(smallest_even) if even_nodes else None
    return [smallest_even, index] if smallest_even and index != None else []