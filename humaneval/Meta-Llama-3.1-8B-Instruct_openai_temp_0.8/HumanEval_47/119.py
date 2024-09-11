### Median Calculator
```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in a sorted list. If the list has an even number of elements, 
    the median is the average of the two middle values.

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
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If the list has an odd number of elements, the median is the middle value
        return sorted_l[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle values
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a function `median` that calculates the median of a given list of numbers. It first sorts the list in ascending order, then determines whether the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle value. If the list has an even number of elements, the median is the average of the two middle values. The script includes example usage at the end to demonstrate the function's behavior.