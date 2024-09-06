```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: Sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This version of the code uses a generator expression instead of the range function. Although both versions of the code are valid, this version is shorter and employs a more common and versatile solution.