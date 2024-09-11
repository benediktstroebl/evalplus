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
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)     # Get the number of elements in the list

    # If the list has an odd number of elements, the median is the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]  # Return the middle value

    # If the list has an even number of elements, the median is the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]  # Get the first middle value
        mid2 = sorted_l[n // 2]     # Get the second middle value
        return (mid1 + mid2) / 2    # Return the average of the two middle values


# Test the function
print(median([3, 1, 2, 4, 5]))   # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the elements in the list. The function first sorts the list in ascending order, then checks if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle value. If the list has an even number of elements, the median is the average of the two middle values. The function is then tested with two examples to demonstrate its usage.