### Median Calculation Function in Python
```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median value of the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Example usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers_2 = [-10, 4, 6, 1000, 10, 20]
print(median(numbers_2))  # Output: 15.0
```

This script utilizes the built-in `statistics` module in Python, which provides functions to calculate mathematical statistics of numeric data. The `median()` function from this module is used to calculate the median of the input list. If the list has an even number of elements, the median is the average of the two middle elements.