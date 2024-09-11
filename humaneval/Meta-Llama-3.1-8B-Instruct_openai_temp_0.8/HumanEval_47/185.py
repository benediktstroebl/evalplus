### Median Calculation
#### A Python Script to Find the Median of a List

```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.
    
    Example usage:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Example usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))
```

This script uses the built-in `statistics` module in Python, which provides functions to calculate mathematical statistics of numeric data, including the median. The `median` function takes a list of numbers as input and returns the median of those numbers.

Please note that the median calculation will return the average of the two middle values if the list has an even number of elements.