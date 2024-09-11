### Median Calculation in Python

The following Python script defines a function `median` that calculates the median of elements in a given list.

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    The median is the middle value in a sorted list of numbers. If the list has an even number of elements,
    the median is the average of the two middle numbers.

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

    # Sort the list in ascending order
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the list has an odd number of elements, the median is the middle value
    if n % 2 == 1:
        return l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle values
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list `l` as input and returns its median. The function first checks if the list is empty and raises a `ValueError` if it is. Then, it sorts the list in ascending order using the `sort` method. After sorting, it checks if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle value. If the list has an even number of elements, the median is the average of the two middle values. The script also includes example usage to demonstrate how to use the `median` function.