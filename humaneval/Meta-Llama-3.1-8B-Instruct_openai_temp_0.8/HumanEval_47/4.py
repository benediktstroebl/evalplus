```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by sorting the list first, then finding the middle value.
    If the list has an even number of elements, the median is the average of the two middle values.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the list using the built-in `sorted()` function. It then checks if the list has an odd or even number of elements. If it has an odd number of elements, it returns the middle value. If it has an even number of elements, it returns the average of the two middle values. The script includes test cases to demonstrate its functionality.