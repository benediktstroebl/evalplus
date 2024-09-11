### Median Calculation in Python
```python
def median(l: list):
    """
    Return median of elements in the list l.

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
    # First, we sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        median = sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        median = (mid1 + mid2) / 2
    
    return median

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```
This Python script defines a function `median` that calculates the median of a list of numbers. It sorts the list, determines whether the length of the list is odd or even, and returns the median accordingly. The script also includes example use cases to demonstrate the function's usage.