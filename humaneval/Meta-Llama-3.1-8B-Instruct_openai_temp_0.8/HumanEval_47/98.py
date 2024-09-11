```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return sorted_list[n // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list, then checks whether the length of the list is odd or even. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements. The script then tests the function with a few examples.