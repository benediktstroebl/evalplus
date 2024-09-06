Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, in accordance with the problem statement:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        min_even_node = min(even_nodes)
        min_index = even_nodes.index(min_even_node)
        return [min_even_node, min_index]
    else:
        return []
```

This function identifies the target node based on the given constraints: it filters out even nodes from the input array, then identifies the smallest even node value and its corresponding index using the `min` and `index` methods. The result is returned as a list `[node_value, node_index]`.

Additionally, if the array has no even nodes, the function returns `[]`, appropriately reflecting that there are no nodes to pluck. 

This solution adheres to the problem's specifications and provides an efficient approach to plucking nodes from the given tree branch. Feel free to test it with various input scenarios to ensure it behaves as expected.