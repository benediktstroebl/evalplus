```python
def add(lst):
    """Add elements at odd indices that are even.

    Args:
        lst (list): A non-empty list of integers.

    Returns:
        int: Sum of even elements at odd indices.

    Examples:
        >>> add([4, 2, 6, 7])
        2
    """
    return sum(x for index, x in enumerate(lst) if index % 2 == 1 and x % 2 == 0)
```