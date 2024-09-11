### Calculating the Median of a List
#### Using Python

Here's a Python function that calculates the median of a list of numbers:

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
```

This function uses the `statistics.median()` function to calculate the median of the list.

If you want to implement the logic manually (without using the `statistics` module), you can use the following code:

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
    
    if n % 2 == 0:
        # If the number of elements is even, the median is the average of the two middle elements
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the number of elements is odd, the median is the middle element
        median = sorted_l[n // 2]
    
    return median
```

This manual implementation first sorts the list in ascending order. Then it checks whether the number of elements is even or odd. If it's even, the median is the average of the two middle elements. If it's odd, the median is the middle element.