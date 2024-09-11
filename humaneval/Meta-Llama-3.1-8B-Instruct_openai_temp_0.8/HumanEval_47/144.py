```python
def median(lst: list):
    """
    Return median of elements in the list lst.

    The function first sorts the list in ascending order and then calculates the median.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    Args:
        lst (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        # If the list has an odd number of elements, the median is the middle element.
        return sorted_lst[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle elements.
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. The function first sorts the list in ascending order, then checks if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. The function returns the calculated median. The script includes example usage of the function.