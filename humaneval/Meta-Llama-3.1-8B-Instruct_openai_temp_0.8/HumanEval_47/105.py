```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    
    # Sort the list
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script uses the built-in `sorted()` function to sort the list. It then determines whether the list has an odd or even number of elements and calculates the median accordingly. If the list is odd, the median is the middle element. If the list is even, the median is the average of the two middle elements.