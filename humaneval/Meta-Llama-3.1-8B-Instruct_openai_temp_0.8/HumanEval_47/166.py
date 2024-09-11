```python
def median(l: list):
    """
    Return median of elements in the list l.

    The input list l can have any number of elements, and it can be sorted or unsorted.
    If the length of l is odd, the median is the middle element.
    If the length of l is even, the median is the average of the two middle elements.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in l.

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
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the length of the list is odd, return the middle element
    if n % 2!= 0:
        return l[n // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        mid1 = l[n // 2 - 1]
        mid2 = l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```