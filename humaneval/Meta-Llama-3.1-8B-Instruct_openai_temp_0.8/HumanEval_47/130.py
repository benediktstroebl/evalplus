```python
def median(l: list):
    """
    Return median of elements in the list l.

    The list must contain an even or odd number of elements.

    For even-length lists, the median is the average of the two middle elements.
    For odd-length lists, the median is the middle element.

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
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)     # Get the length of the list

    if n % 2 == 0:        # If the list has an even number of elements
        mid1 = sorted_l[n // 2 - 1]  # The first middle element
        mid2 = sorted_l[n // 2]     # The second middle element
        median = (mid1 + mid2) / 2  # The median is the average of the two middle elements
    else:                 # If the list has an odd number of elements
        median = sorted_l[n // 2]  # The median is the middle element

    return median

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It sorts the list in ascending order and then checks if the length of the list is even or odd. If the length is even, it calculates the median as the average of the two middle elements. If the length is odd, it calculates the median as the middle element. The function returns the median. The script then tests the function with the provided examples.