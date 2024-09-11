### Median Calculation
#### A Python Script to Find the Median of a List

```python
import statistics

def median(l: list) -> float:
    """
    Return the median of elements in the list l.

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

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the built-in `statistics.median` function from Python's standard library, which efficiently calculates the median of a list of numbers. It handles both even and odd-length lists correctly. If the input list is not valid (for example, it contains non-numeric elements), this implementation will raise an exception when trying to calculate the median.