### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by sorting the list first, then checking if
    the list length is even or odd. If it's even, the median is the average
    of the two middle numbers. If it's odd, the median is the middle number.

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
    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list is empty, raise a ValueError
    if n == 0:
        raise ValueError("Cannot calculate median of an empty list")

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]

    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a given list of numbers. It first sorts the list in ascending order, then checks if the list length is even or odd. If it's even, it returns the average of the two middle numbers. If it's odd, it returns the middle number. The script also includes example usage to demonstrate the function's behavior.