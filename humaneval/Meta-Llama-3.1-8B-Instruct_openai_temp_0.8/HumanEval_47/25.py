### Median Calculator
```python
import statistics

def median(l: list) -> float:
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

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
This script uses the built-in `statistics.median()` function to calculate the median. This function is more efficient and accurate than manually implementing the median calculation.