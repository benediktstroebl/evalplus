```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
    l (list): A list containing elements to be made unique

    Returns:
    list: A sorted list of unique elements

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then convert it back to a list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    unique_list.sort()
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in `set` data structure in Python to remove duplicates from the list and then converts it back to a list. Finally, it sorts the list in ascending order and returns it.

However, a more efficient way to solve this problem is to use a combination of a `set` and the `sorted` function, which would look like this:

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
    l (list): A list containing elements to be made unique

    Returns:
    list: A sorted list of unique elements

    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This version of the script is more efficient because it doesn't require converting the list to a set and back again, which can be expensive for large lists.