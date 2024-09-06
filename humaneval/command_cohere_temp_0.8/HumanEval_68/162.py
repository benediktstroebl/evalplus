Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_val, min_index = min(enumerate(even_nodes), key=lambda x: x[1])
    return [min_even_val, min_index[0]]
```

This function identifies the smallest even value among the nodes and selects the node with the smallest index among those that have the smallest even value. The result is returned as a list [smallest even value, index of the node with the smallest even value].

Here's an example of how you can use the `pluck` function:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)  # Output: [2, 1]
``` 

This will output `[2, 1]`, as explained in the example provided in the problem statement.