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

This function identifies even nodes, finds the smallest even node, and locates its index. Subsequently, it returns a list consisting of the smallest even value along with its corresponding index. In the event that no even nodes are present, the function returns an empty list.

Here's an example of how you can use this function:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

For the given example, the output would be:
```
[2, 1]
```

This exemplifies the function's capability to identify the node with the smallest even value (2) and determine that its index is 1.