```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): Input list

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Use a set to remove duplicate elements
    unique_elements = set(l)
    # Convert the set back to a list and sort it
    sorted_list = sorted(list(unique_elements))
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicate elements using a set, and returns the sorted list of unique elements. The function is then tested with the provided example.