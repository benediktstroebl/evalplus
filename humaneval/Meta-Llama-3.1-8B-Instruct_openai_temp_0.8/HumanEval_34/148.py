### Unique Elements in a List
```python
def unique(l: list) -> list:
    """Return sorted unique elements in a list

    Args:
        l (list): A list of elements

    Returns:
        list: A sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list `l` as input and returns a sorted list of unique elements. The function uses the `set` function to create a set of unique elements, which is then converted back to a list and sorted using the `sorted` function.