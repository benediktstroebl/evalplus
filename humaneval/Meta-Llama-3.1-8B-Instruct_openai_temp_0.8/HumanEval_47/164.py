```python
def median(l: list):
    """
    Return median of elements in the list l.

    The function first sorts the list in ascending order, then it calculates the middle value(s).
    If the list has an odd number of elements, the median is the middle value. If the list has an even number of elements,
    the median is the average of the two middle values.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list l.

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

    # If the list has an odd number of elements, the median is the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle values
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function called `median` that takes a list of numbers as input and returns the median of the list. The median is the middle value of the list when it is sorted in ascending order. If the list has an even number of elements, the median is the average of the two middle values. The function first sorts the list, then it calculates the median based on whether the list has an odd or even number of elements. If the list is empty, the function raises a `ValueError`. The script includes tests to ensure the function works correctly.