### Median Calculation in Python
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

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
Note that we are using the built-in `statistics.median()` function in Python's standard library to calculate the median. This function handles both even and odd lengths of the input list correctly. If you're interested in implementing the median calculation manually, we can provide an alternative solution as well.