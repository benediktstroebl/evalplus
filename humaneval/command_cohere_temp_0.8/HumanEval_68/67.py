Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch, adhering to the problem statement:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This function identifies even nodes within the array and finds the smallest even value among them. If there are multiple nodes with the same smallest even value, it selects the one with the smallest index. The result is returned as a list in the format [smallest even value, its index]. If there are no even values in the array, the function returns an empty list.

Here is an example usage of this function:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)  # Output: [2, 1]
``` 
This will return the node with the smallest even value (2) and its index (1) in the given array.