### Median Calculator
#### Python Script
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

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script uses the built-in `statistics.median()` function in Python to calculate the median of a list of numbers. This approach is concise and efficient, making it a good choice for solving this problem.

However, if you want to implement the median calculation manually, here is an alternative version of the script:
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
    sorted_l = sorted(l)
    n = len(l)
    
    if n % 2 == 0:
        # If the list has an even number of elements, the median is the average of the two middle elements
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element
        median = sorted_l[n // 2]
    
    return median

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This manual implementation also requires sorting the list, but the rest of the logic is straightforward.