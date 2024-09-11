```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list elements.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Testing the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the `statistics.median()` function to calculate the median of the input list. The `statistics` module is part of Python's standard library and provides functions for calculating mathematical statistics of numeric data. The `median()` function returns the median of the input list, which is the middle value when the list is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle values.