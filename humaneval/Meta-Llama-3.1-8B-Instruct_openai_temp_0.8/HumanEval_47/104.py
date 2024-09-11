### Median Calculation Script
```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

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
    if not l:
        raise ValueError("Cannot calculate median of an empty list")
    return statistics.median(l)

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script uses the built-in `statistics` module in Python to calculate the median of a list. This is more efficient and concise than implementing the median calculation from scratch. The script also includes a check to raise a `ValueError` if the input list is empty, since the median is not defined for an empty list.