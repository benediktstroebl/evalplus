from collections import *
def pluck(arr):
    # your task is to pluck one of the nodes and return it
    if not arr or not isinstance(arr, Container): return []

    # create a dictionary to hold the nodes with even values and their indices
    even_nodes = {}

    # iterate over the array and populate the dictionary
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even_nodes[n] = i

    # if the dictionary is empty, return an empty list
    if not even_nodes: return []

    # if there is only one node with the smallest even value, return it
    if len(even_nodes) == 1:
        return [even_nodes.values().pop(), even_nodes.keys().pop()]

    # if there are multiple nodes with the smallest even value, select the one with the smallest index
    smallest_index = min(even_nodes.values())
    return [even_nodes[smallest_index], smallest_index]