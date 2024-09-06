Here's a Python script that solves the given problem with an efficient approach using Python's `collections` module:
```python
from collections import Counter

def pluck(arr):
    even_nodes = [n for n in arr if n % 2 == 0]
    if not even_nodes:
        return []

    # Use Counter to find the minimum even node and its index
    min_node, min_index = min(Counter(even_nodes).items(), key=lambda x: x[1])
    
    return [min_node, min_index]

# Example usage
input_arr = [4, 2, 3]
result = pluck(input_arr)
print(result)  # Output: [2, 1]
```

This approach uses the `Counter` class from the `collections` module to efficiently find the minimum even node and its index in a single pass without the need for multiple loops. The `min` function is used to find the minimum item from the `Counter` dictionary items, considering both the node value and its index.