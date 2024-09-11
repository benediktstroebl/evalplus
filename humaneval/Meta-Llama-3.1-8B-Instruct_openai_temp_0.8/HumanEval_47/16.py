```python
def median(l: list):
    """Return median of elements in the list l.
    
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
    if not l:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length of the list is odd, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the length of the list is even, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines the `median` function to calculate the median of a list of numbers. It first checks if the list is empty, and raises a `ValueError` if it is. Then, it sorts the list in ascending order, gets its length, and calculates the median based on whether the length is odd or even. Finally, it tests the function with the provided examples.