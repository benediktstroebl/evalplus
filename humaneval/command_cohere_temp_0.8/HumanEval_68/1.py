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

This script includes a standalone `pluck` function that accepts an array as input. The function initially filters the array to isolate even nodes and identifies the smallest even node using the `min` function. If there are no even nodes, the function returns a list containing an empty list. The script then locates the index of the smallest even node through the `index` attribute of the `min` function. The function returns a list containing the smallest even value and its corresponding index. 

The `pluck` function adheres to the problem's specified constraints and is equipped to handle a variety of scenarios. It achieves this through an efficient and singular approach, making it a robust solution.