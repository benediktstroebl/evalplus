```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique()` that takes a list as input, removes duplicates by converting it to a set, and then converts it back to a list and sorts it. The result is a sorted list of unique elements. The script then tests this function with the provided example.