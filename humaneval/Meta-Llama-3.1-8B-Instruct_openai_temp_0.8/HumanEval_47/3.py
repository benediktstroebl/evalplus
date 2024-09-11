### Median of a List
#### Solution

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the given list.
    
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
    
    # If the length is odd, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the length is even, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a given list of numbers. It sorts the list in ascending order and then determines whether the length of the list is odd or even. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements. The script includes docstrings for the function to provide documentation and examples of usage.