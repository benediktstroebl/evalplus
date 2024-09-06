Here's a Python script that includes a self-contained function designed to solve the problem presented:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This function identifies even nodes using a list comprehension and finds the index of the smallest even node using the `min` and `index` methods. The result is a list containing the smallest even node and its corresponding index. If there are no even-valued nodes in the array, an empty list is returned.