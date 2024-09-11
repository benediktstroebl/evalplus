### Unique Elements in a List
#### Problem Description
Return sorted unique elements in a list.

#### Solution
```python
def unique(l: list):
    """
    Return sorted unique elements in a list
    
    Args:
    l (list): Input list of elements
    
    Returns:
    list: Sorted list of unique elements
    
    Examples:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    sorted_unique_list = sorted(list(unique_set))
    
    return sorted_unique_list

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input and returns a sorted list of unique elements. It uses a set to remove duplicates and then converts the set back to a list and sorts it using the `sorted` function. The example usage at the end demonstrates how to use the `unique` function.