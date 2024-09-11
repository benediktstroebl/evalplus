```python
import statistics

def median(l: list):
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of elements to calculate the median from.
    
    Returns:
    float: The median of the input list.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Testing the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

However, if you want to implement it manually without using the built-in `statistics.median()` function, you can use the following code:

```python
def median(l: list):
    """Return median of elements in the list l.
    
    Args:
    l (list): A list of elements to calculate the median from.
    
    Returns:
    float: The median of the input list.
    
    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:  # even number of elements
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:  # odd number of elements
        median = sorted_l[n // 2]
    
    return median

# Testing the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```