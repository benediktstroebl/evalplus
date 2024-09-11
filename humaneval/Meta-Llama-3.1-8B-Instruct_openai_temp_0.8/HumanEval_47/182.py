### Median Calculation in Python
#### Function Definition and Usage

```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.
    
    :param l: A list of numbers.
    :return: The median of the numbers in the list.
    
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This script uses the `statistics` module in Python's standard library to calculate the median. The `median()` function from this module takes an iterable of numbers and returns the median. This approach is concise and effective for calculating medians.

The provided docstring explains the purpose of the function, its parameters, and its return value, along with some example usage. The example usage at the end demonstrates how to call the `median()` function with two different lists of numbers.