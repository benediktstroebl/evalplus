```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
        l (list): A list of elements

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
    
    # Return the sorted list of unique elements
    return unique_list

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, removes duplicates by converting it to a set, and then sorts the unique elements in ascending order. The function returns the sorted list of unique elements. The example usage at the end demonstrates how to use this function to solve the problem.