```python
def median(l: list):
    """Return median of elements in the list l.
    
    The function first checks if the list is empty. If it is, the function raises a ValueError.
    If the list has an odd number of elements, the function returns the middle element.
    If the list has an even number of elements, the function returns the average of the two middle elements.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
    
    Raises:
        ValueError: If the list is empty.
        
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if not l:
        raise ValueError("Cannot calculate median of an empty list")
    
    sorted_l = sorted(l)
    
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle element
        return sorted_l[n // 2]
    else:
        # If the list has an even number of elements, return the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first checks if the list is empty and raises a `ValueError` if it is. Then it sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. The function returns the median as a float. The script includes test cases to demonstrate the function's behavior.