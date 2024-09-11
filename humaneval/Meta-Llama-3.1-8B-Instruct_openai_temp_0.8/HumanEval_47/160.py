```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    The median is the middle value in a sorted list of numbers.
    If the list has an even number of elements, the median is the average
    of the two middle values.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    n = len(l)
    # Sort the list
    l.sort()
    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return l[n // 2]
    # If the list has an even number of elements, return the average of the two middle values
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2

# Test cases
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and then determines the median based on whether the list has an odd or even number of elements. The function returns the median as a float. The script also includes test cases to demonstrate the function's behavior.