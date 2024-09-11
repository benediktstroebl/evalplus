```python
import statistics

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
    return statistics.median(l)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This script uses the built-in `statistics` module in Python, which provides functions for calculating mathematical statistics of numeric data. The `median` function in this script simply calls `statistics.median` to calculate the median of the input list.

Alternatively, you can implement the `median` function manually without using the `statistics` module:

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
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```