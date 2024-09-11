```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Check if the list is empty
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the length of the list is odd, return the middle element
    if n % 2 == 1:
        return l[n // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2


# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first checks if the list is empty and raises a `ValueError` if it is. Then it sorts the list and calculates the median based on whether the length of the list is odd or even. If the length is odd, it returns the middle element; if the length is even, it returns the average of the two middle elements. The script includes example usage at the end to demonstrate how to use the `median` function.