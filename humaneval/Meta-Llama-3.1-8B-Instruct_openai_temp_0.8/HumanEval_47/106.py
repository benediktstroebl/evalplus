```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Raises:
        ValueError: If the input list is empty.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return sorted_l[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Example use cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first checks if the input list is empty, and raises a `ValueError` if it is. It then sorts the list and calculates the median based on whether the length of the list is odd or even. If the length is odd, the median is the middle element, and if the length is even, the median is the average of the two middle elements. The script also includes example use cases to demonstrate the usage of the `median` function.