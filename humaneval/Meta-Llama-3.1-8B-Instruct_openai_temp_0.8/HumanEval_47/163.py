```python
def median(l: list):
    """Return median of elements in the list l.
    
    The list must be non-empty.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the numbers in the list.
    
    Raises:
        ValueError: If the list is empty.
        
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Input list is empty.")
    
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle number
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle numbers
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a given list of numbers. The function first checks if the list is empty and raises a `ValueError` if it is. Then it sorts the list in ascending order and calculates the median based on whether the length of the list is odd or even. If the length is odd, the median is the middle number. If the length is even, the median is the average of the two middle numbers. The function is then tested with two example lists.