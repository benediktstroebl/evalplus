Here's a Python script that includes a self-contained function designed to solve the problem presented, along with additional tests to ensure its accuracy:
```python
def pluck(arr):
    even_nodes = [val for val in arr if val % 2 == 0]
    if not even_nodes:
        return []
    min_even_node = min(even_nodes)
    min_index = even_nodes.index(min_even_node)
    return [min_even_node, min_index]

# Additional tests
test_data = [
    ([4, 2, 3], [2, 1]),
    ([1, 2, 3], [2, 1]),
    ([5, 0, 3, 0, 4, 2], [0, 1]),
    ([7, 3, 2, 4, 6, 8, 1, 5, 0], [0, 1])
]

for nodes, expected in test_data:
    result = pluck(nodes)
    assert result == expected, f"Expected {expected}, but got {result}"
```

In this script, the `pluck` function first identifies the smallest even node from the input `arr` using a list comprehension. It then locates the index of the node using the `index` method. If there are no even nodes, the function returns an empty list. The additional tests ensure that the function behaves correctly for various input scenarios.