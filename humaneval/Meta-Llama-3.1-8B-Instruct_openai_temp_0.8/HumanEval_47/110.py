### Median Calculation Script

Here's a Python script that uses the built-in `statistics` module to calculate the median of a given list of numbers:

```python
import statistics

def median(numbers: list):
    """
    Return the median of elements in the list.

    Args:
        numbers: A list of numbers.

    Returns:
        The median of the numbers in the list.
    """
    try:
        return statistics.median(numbers)
    except statistics.StatisticsError:
        raise ValueError("List must not be empty")

# Example usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This script uses the `statistics.median()` function to calculate the median of the list. If the list is empty, it raises a `ValueError`. The example usage section demonstrates how to use the `median()` function with different lists of numbers.