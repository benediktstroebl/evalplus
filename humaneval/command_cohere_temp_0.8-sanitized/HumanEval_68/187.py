from collections import Counter
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    return [(min(even_nodes), min(Counter(even_nodes).items(), key=lambda item: item[1]))[0] if even_nodes else []]