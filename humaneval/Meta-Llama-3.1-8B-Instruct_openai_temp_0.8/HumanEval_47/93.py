```python
def median(l: list):
    """Return median of elements in the list l.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the list.

    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)    # Get the number of elements in the list
    if n % 2 == 0:       # If the number of elements is even
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2  # Calculate the median as the average of the two middle elements
    else:                # If the number of elements is odd
        median = sorted_l[n // 2]  # The median is the middle element
    return median

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, and then checks if the number of elements is even or odd. If it's even, it calculates the median as the average of the two middle elements. If it's odd, it returns the middle element as the median. The script then tests the function with two examples.