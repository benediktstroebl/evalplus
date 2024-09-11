### Median Calculation in Python
#### Using the built-in `statistics` module
```python
import statistics

def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list l.

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

#### Alternatively, you can implement the median calculation manually
```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list l.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 0:
        # If the list has an even number of elements, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the list has an odd number of elements, the median is the middle element
        return sorted_l[n // 2]

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

Both of these scripts define a function `median` that calculates and returns the median of the elements in the list `l`. The first script uses the `statistics.median` function from the built-in `statistics` module, while the second script implements the median calculation manually using the sorted list of numbers.