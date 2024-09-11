```python
def unique(input_list: list) -> list:
    """
    Return sorted unique elements in a list.

    Args:
        input_list (list): Input list containing duplicate elements.

    Returns:
        list: Sorted list with unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_set))
    
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses a set to remove duplicates and then sorts the resulting list. Note that sets in Python are unordered, so we need to convert it back to a list and sort it before returning the result. The `sorted()` function returns a new list containing the sorted elements from the original list.