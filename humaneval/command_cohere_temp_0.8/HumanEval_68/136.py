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

This function identifies even nodes in the `arr` array and selects the smallest one. If there are multiple occurrences of the smallest even value, it selects the one with the smallest index. The result is a list containing the smallest even value and its index. The function returns an empty list if no even nodes are found. 

Here is an example of how you can use this function:
```python
arr = [4,2,3]
result = pluck(arr)
print(result)
```

The output will be:
```
[2, 1]
```

This demonstrates the function's ability to identify the smallest even value (2) in the array and return its index (1).