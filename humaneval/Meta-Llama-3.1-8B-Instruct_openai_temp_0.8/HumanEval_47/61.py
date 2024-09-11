```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    The median is the middle value in an ordered integer list. It is the 
    "middle number" in a sorted, ascending or descending, list of numbers.

    If the list has an even number of elements, the median is the average 
    of the two middle numbers.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    # First, sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts it in ascending order, and then finds the median based on whether the list has an odd or even number of elements. If the list has an odd number of elements, it returns the middle value. If the list has an even number of elements, it returns the average of the two middle values. The script also includes test cases to demonstrate the function's behavior.