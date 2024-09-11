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

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script uses the `statistics` module's `median` function to calculate the median of the input list, making it more concise and efficient than implementing the calculation from scratch.