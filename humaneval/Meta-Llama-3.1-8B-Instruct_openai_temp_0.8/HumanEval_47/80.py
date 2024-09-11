Here's a Python script that calculates the median of a list of numbers. This script uses the `statistics` module to calculate the median.

```markdown
### Median Calculation Script

This script calculates the median of a given list of numbers.

```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float or int: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(l)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(f"Median of {numbers}: {median(numbers)}")

numbers = [-10, 4, 6, 1000, 10, 20]
print(f"Median of {numbers}: {median(numbers)}")
```

This script first imports the `statistics` module, which provides functions for calculating mathematical statistics of numeric data. It then defines a function `median` that takes a list of numbers as input and returns the median of these numbers using the `statistics.median` function.

Finally, the script includes an example usage section where it calculates and prints the median of two different lists of numbers.

Note: The `statistics.median` function used here can handle lists of both even and odd lengths. For lists of even length, it returns the average of the two middle numbers.