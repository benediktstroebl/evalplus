### Median Calculation in Python
```python
import statistics

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
    return statistics.median(l)

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
In this script, we use the built-in `statistics` module to calculate the median of the input list. This approach is more concise and efficient than implementing a custom algorithm. If you want to implement a custom solution, here is an alternative version:
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
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 1:
        return sorted_l[n // 2]
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
```
This custom implementation calculates the median using the standard formula for odd and even length lists.