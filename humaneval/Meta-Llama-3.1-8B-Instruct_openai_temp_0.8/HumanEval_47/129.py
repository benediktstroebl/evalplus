Here's a Python function that calculates the median of a list of numbers:

```python
import statistics

def median(lst: list):
    """Return median of elements in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(lst)

# Test cases
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

However, if you prefer to calculate the median manually, here's an alternative implementation:

```python
def median(lst: list):
    """Return median of elements in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 0:
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        median = sorted_lst[n // 2]
    
    return median

# Test cases
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

Both scripts calculate the median of a list of numbers, but the second one uses a manual implementation for demonstration purposes. In a real application, you would generally use the `statistics.median()` function provided by the Python standard library for its simplicity and efficiency.