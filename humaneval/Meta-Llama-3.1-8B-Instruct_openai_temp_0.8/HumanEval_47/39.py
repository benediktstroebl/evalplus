```python
def median(l: list):
    """
    Returns the median of the elements in the list l.

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
    # Sort the list in ascending order
    l.sort()
    
    # Get the length of the list
    n = len(l)
    
    # If the length of the list is odd, return the middle element
    if n % 2!= 0:
        return l[n // 2]
    
    # If the length of the list is even, return the average of the two middle elements
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that takes a list of numbers and returns its median. It first sorts the list in ascending order, then checks whether the length of the list is odd or even. If it's odd, it returns the middle element. If it's even, it returns the average of the two middle elements. The function is then tested with two examples.