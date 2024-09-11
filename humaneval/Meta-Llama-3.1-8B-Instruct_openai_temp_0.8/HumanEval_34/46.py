```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        lst (list): Input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(lst)
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Alternatively, you can use a one-liner solution:

```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list

    Args:
        lst (list): Input list

    Returns:
        list: Sorted list of unique elements
    """
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```