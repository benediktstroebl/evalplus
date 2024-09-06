Here's a Python script that solves the given problem with an efficient approach using Python's built-in functionalities, no third-party packages, and a concise code snippet:
```python
def pluck(arr):
    even_nodes = [i for i in arr if i % 2 == 0]
    if even_nodes:
        return [min(even_nodes), even_nodes.index(min(even_nodes))]
    else:
        return []
```
This approach does not rely on additional packages and leverages Python's list comprehension and built-in functions for a concise and efficient solution.