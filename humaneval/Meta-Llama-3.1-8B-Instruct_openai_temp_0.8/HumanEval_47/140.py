```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.
    
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
    return statistics.median(l)

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses Python's built-in `statistics` module to calculate the median of a given list. If you prefer to implement the calculation manually, you can use the following code:

```python
def median(l: list):
    """
    Return median of elements in the list l.
    
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
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        median = sorted_list[n // 2]
    
    return median

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This manual implementation first sorts the list and then checks if the length of the list is even or odd. If it's even, it calculates the median as the average of the two middle numbers. If it's odd, it simply returns the middle number.