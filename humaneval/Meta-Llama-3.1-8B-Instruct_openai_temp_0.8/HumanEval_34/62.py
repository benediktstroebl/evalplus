### Unique Elements in a List
```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list

    Args:
        lst (list): The input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list as input, removes duplicates using a set, and returns the sorted list of unique elements. The `sorted` function is used to ensure the output is sorted in ascending order.