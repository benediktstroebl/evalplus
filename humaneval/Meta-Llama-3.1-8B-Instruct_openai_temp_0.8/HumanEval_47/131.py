### Median Calculation in Python
Here's a Python script that calculates the median of a given list of numbers. This script uses the built-in `sorted` function to sort the list, then finds the median.

```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        The median of the numbers in the list. If the list has an odd number of elements, the median is the middle element.
        If the list has an even number of elements, the median is the average of the two middle elements.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """

    # Check if the list is empty
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]

    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

However, if you want a more efficient solution, consider using the `np.median` function from the NumPy library, which is specifically designed for this purpose.

```python
import numpy as np

def median(l: list):
    """Return median of elements in the list l."""
    return np.median(l)

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```