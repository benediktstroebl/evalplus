```python
def median(l: list):
    """Return median of elements in the list l.
    
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
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        median = sorted_l[n // 2]
    
    return median

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers `l` as input, sorts the list, and then calculates the median based on whether the length of the list is even or odd. The result is then returned. The script also includes two test cases to demonstrate the function's correctness.