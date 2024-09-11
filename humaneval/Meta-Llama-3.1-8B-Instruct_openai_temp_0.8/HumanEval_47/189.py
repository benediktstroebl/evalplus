### Median Calculator in Python

```python
import statistics

def median(l: list) -> float:
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
    return statistics.median(l)

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

In this script, we're using the `statistics` module in Python, which provides functions to calculate mathematical statistics of numeric data. The `median()` function from the `statistics` module calculates the median of the elements in the given list. 

Note that the `median()` function returns the median as a float, even if the list has an odd number of elements. This is because the median can be a floating-point number in some cases, especially when there are two middle values with different ranks (which happens when the list has an even number of elements).