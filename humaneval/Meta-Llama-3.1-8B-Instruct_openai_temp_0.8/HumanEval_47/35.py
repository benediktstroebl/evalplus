```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in a sorted list of numbers. If the list has an even number of elements,
    the median is the average of the two middle numbers.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle number
    if n % 2 == 1:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle numbers
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that takes a list of numbers as input, sorts the list in ascending order, and then calculates the median based on whether the list has an odd or even number of elements. The median is then returned as a float. The script includes docstrings and examples to illustrate how to use the function.