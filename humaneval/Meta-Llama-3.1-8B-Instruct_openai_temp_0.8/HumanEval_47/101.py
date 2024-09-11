### Median Calculator Script
```python
def median(l: list) -> float:
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    float: The median of the elements in the list l.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return float(sorted_l[n // 2])
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```
This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then checks if the length of the list is odd or even. If it's odd, it returns the middle element as the median. If it's even, it returns the average of the two middle elements as the median. The function is then tested with two example lists.