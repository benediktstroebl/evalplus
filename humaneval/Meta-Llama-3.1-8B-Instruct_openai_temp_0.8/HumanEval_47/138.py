```python
def median(l: list):
    """
    Returns the median of elements in the list l.
    
    The median is the middle value in a sorted list. If the list has an even number of elements, 
    the median is the average of the two middle elements.

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
    n = len(sorted_l)  # Get the number of elements in the list

    # If the list is empty, raise a ValueError
    if n == 0:
        raise ValueError("Cannot calculate median of an empty list")

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the input list in ascending order. It then checks if the list is empty, in which case it raises a ValueError. If the list has an odd number of elements, it returns the middle element. If the list has an even number of elements, it returns the average of the two middle elements. The function is then tested with the provided examples.