Here's a Python script that includes a self-contained function designed to pluck a node from a tree branch represented by an array, following the problem statement you provided:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]

# Example usage
input_branch = [4, 2, 3]
result = pluck(input_branch)
print(result)  # Output: [2, 1]
```

This script includes a standalone `pluck` function that:
1. Collects an array of even nodes from the input branch.
2. Finds the minimum value among these even nodes.
3. Determines the index of the minimum even node.
4. Returns a list containing the minimum even node value and its index.

The example usage demonstrates how to call the `pluck` function with an example input branch, and the output prints the result accordingly.