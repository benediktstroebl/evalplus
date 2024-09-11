```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the elements in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list
    l.sort()
    
    # Get the length of the list
    n = len(l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Should print 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Should print 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the elements in the list. It first checks if the list is empty, and if so, raises a `ValueError`. It then sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. The function includes docstrings to provide documentation and examples of usage.