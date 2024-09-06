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

This function identifies even nodes in the `arr` array and selects the smallest one. If there are several smallest even nodes, it chooses the one at the earliest index. The result is a list containing the smallest even node and its index. 

Here's an example of how to use this function:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

For the given example, the output would be:
```
[2, 1]
```

This exemplifies how the function selects the node with the smallest even value (2) and acknowledges its index (1).