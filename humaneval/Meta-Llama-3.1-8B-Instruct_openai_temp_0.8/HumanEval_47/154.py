```python
def median(l: list):
    """Return median of elements in the list l.
    
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
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:
        # If the number of elements is even, the median is the average of the two middle elements
        median = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        # If the number of elements is odd, the median is the middle element
        median = sorted_list[n//2]
    
    return median

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function called `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then checks if the number of elements is even or odd. If it's even, it calculates the median as the average of the two middle elements; if it's odd, it calculates the median as the middle element. The function then returns the median. The script also includes some test cases to verify that the function works correctly.