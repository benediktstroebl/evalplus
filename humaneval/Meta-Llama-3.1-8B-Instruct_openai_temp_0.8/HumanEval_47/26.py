```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    l = sorted(l)

    # Get the length of the list
    n = len(l)

    # If the length of the list is even, the median is the average of the two middle numbers
    if n % 2 == 0:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2
    # If the length of the list is odd, the median is the middle number
    else:
        return l[n // 2]


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of these numbers. It first checks if the list is empty, and if so, raises a `ValueError`. Then, it sorts the list in ascending order and calculates the median based on whether the length of the list is even or odd. The script also includes two test cases to demonstrate the function's correctness.