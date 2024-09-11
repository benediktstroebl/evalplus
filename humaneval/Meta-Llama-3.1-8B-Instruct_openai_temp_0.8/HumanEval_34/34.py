### Unique Elements in a List
#### Problem: Return sorted unique elements in a list
```python
def unique(l: list):
    """Return sorted unique elements in a list
    Args:
        l (list): The input list
    Returns:
        list: A sorted list of unique elements from the input list
    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```
This script defines a function `unique` that takes a list `l` as input, converts it to a set (which removes duplicates) and then converts it back to a list and sorts it. The sorted list of unique elements is then returned.

The `sorted` function returns a new sorted list from the elements of any sequence. The `set` data structure in Python is an unordered collection of unique elements.