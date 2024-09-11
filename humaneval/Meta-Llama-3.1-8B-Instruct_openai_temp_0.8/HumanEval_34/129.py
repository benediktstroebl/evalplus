```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        lst (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
```

This script defines a function `unique` that takes a list as input, removes duplicates using a set, and then sorts the resulting list. The `sorted` function is stable, meaning it maintains the relative order of equal elements, so the original order of first occurrence of each element is preserved in the sorted output.