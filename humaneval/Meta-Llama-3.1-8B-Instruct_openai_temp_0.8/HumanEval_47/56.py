### Computing the Median of a List

Below is a Python script that defines a function `median` to calculate the median of a given list of numbers.

```python
def median(lst: list):
    """Return median of elements in the list lst.
    
    If the list has an even number of elements, the median is the average of the two middle elements.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the elements in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    
    # Sort the list in ascending order
    sorted_lst = sorted(lst)
    
    # Get the length of the list
    n = len(sorted_lst)
    
    # If the list is empty, raise a ValueError
    if n == 0:
        raise ValueError("Cannot compute median of an empty list")
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_lst[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2


# Test the function with examples
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script first sorts the input list in ascending order and then determines whether the list has an odd or even number of elements. If the list has an odd number of elements, it returns the middle element as the median. If the list has an even number of elements, it returns the average of the two middle elements as the median. The script also includes error handling to raise a ValueError if the input list is empty.