```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): Input list
    
    Returns:
        list: Sorted list of unique elements
    """
    # Convert the list to a set to remove duplicates and then convert it back to a list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    sorted_list = sorted(unique_list)
    
    # Return the sorted list of unique elements
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the resulting list in ascending order. The function returns this sorted list of unique elements. The test case at the end demonstrates the function's usage with the provided example input.