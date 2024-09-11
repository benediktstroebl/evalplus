```python
def median(l: list):
    """Return median of elements in the list l.
    
    The median is calculated by sorting the list and finding the middle value.
    If the list has an even number of elements, the median is the average of the two middle values.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
    
    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle value
    if n % 2 == 1:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, return the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and calculates the median. If the list has an odd number of elements, the median is the middle value. If the list has an even number of elements, the median is the average of the two middle values. The script then tests the function with two examples.