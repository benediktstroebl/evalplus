Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch, adhering to the problem statement:
```python
def pluck(arr):
    even_nodes = [x for x in arr if x % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]
```

This function identifies even nodes using a list comprehension and finds the index of the smallest even node using the `index` method. It subsequently returns a list containing the smallest even node and its corresponding index.

Here's an example of how you can use the `pluck` function with a sample input:
```python
arr = [4, 2, 3]
result = pluck(arr)
print(result)
```

For the input array `[4, 2, 3]`, the expected output would be `[2, 1]`, as explained in the problem statement. The function chooses the node with a value of `2` since it has the smallest even value, and because there are multiple nodes with the same smallest even value, it selects the node at index `1` because it has the smallest index.