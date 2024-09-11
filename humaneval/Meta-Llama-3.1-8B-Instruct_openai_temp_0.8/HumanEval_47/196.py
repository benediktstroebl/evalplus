**Calculating Median of a List in Python**
==============================================

Below is a Python function that calculates the median of a list of integers.

```python
def median(l: list):
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    float: The median of the elements in the list.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("The list cannot be empty")
    
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length of the list is even, the median is the average of the two middle numbers
    if n % 2 == 0:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
    
    # If the length of the list is odd, the median is the middle number
    else:
        return sorted_l[n // 2]

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This function first sorts the list in ascending order. Then it checks whether the length of the list is even or odd. If it's even, the median is the average of the two middle numbers. If it's odd, the median is the middle number. The function raises a `ValueError` if the list is empty.