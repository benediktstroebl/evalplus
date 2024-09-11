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
    # First, we need to sort the list in ascending order
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the elements in the list. The function first sorts the list in ascending order, then determines whether the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. The script then tests the function with two example lists.