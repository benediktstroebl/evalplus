```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list containing elements of any type

    Returns:
        list: A sorted list containing unique elements from the input list

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    unique_list = sorted(list(unique_set))
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting the list to a set, and then sorts the resulting set before returning it as a list. The example use case demonstrates the function's behavior on a list with multiple duplicates.