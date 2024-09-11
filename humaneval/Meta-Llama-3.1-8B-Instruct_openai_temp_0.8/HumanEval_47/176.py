### Median of a List
#### Problem Statement
The goal is to write a Python function that calculates the median of a given list of numbers.

#### Solution
```python
import statistics

def median(l: list):
    """Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if not l:
        raise ValueError("Cannot calculate median of an empty list")
    return statistics.median(l)
```
#### Explanation
The solution uses the built-in `statistics` module in Python to calculate the median. If the list is empty, a `ValueError` is raised. Otherwise, the `median` function from the `statistics` module is called to calculate the median.

Note: The median is defined as the middle value in a sorted list. If the list has an even number of elements, the median is the average of the two middle values.

#### Example Use Cases
```python
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([]))  # Raises ValueError
```