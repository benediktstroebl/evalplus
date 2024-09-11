### Unique Elements in a List
#### Python Script

```python
def unique(lst: list):
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A sorted list with unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, converts it to a set (which removes duplicates), and then converts it back to a list while preserving the original order. The `sorted` function is used to sort the unique elements in ascending order. The function includes a docstring that describes its behavior, including an example usage.