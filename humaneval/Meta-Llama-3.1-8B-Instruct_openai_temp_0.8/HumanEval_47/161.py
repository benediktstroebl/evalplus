```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median of a list of numbers is the middle value when the list is sorted.
    If the list has an odd number of elements, the median is the middle number.
    If the list has an even number of elements, the median is the average of the two middle numbers.

    Args:
        l (list): A list of numbers.

    Returns:
        The median of the numbers in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)

    if n % 2 == 1:
        # If the list has an odd number of elements, the median is the middle number
        return sorted_list[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle numbers
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the numbers in the list. The function first sorts the list in ascending order, then checks if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle number. If the list has an even number of elements, the median is the average of the two middle numbers. The script then tests the function with two examples.