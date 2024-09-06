Here's a Python script that solves the given problem with an efficient approach using dictionaries and sorting:
```python
def pluck(arr):
    even_nodes = {node: index for index, node in enumerate(arr) if node % 2 == 0}
    if not even_nodes:
        return []
    min_value, min_index = min(even_nodes.items()), min(even_nodes, key=even_nodes.get)
    return [min_value, min_index]
```
This approach uses a dictionary to efficiently track and retrieve the index for each even node, and then uses the `min` function with a custom key function to find the node with the smallest index and value. This solution is efficient in terms of time and memory complexity. 

The `pluck` function takes an input array `arr` and returns a list containing the plucked node's value and its index, or an empty list if no even nodes are found or the array is empty.