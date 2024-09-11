### Unique Elements in a List
#### Python Script

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
    # Convert the list to a set to remove duplicates, then convert back to list
    # Sort the list to ensure the output is in ascending order
    return sorted(list(set(l)))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique()` that takes a list `l` as input, removes duplicates using a set, converts it back to a list, and then sorts the list in ascending order. The function is then tested with an example list.