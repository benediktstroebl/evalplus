### Median of a List in Python
#### Solution

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
    
    # First, we need to sort the list
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd length, the median is the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the list has an even length, the median is the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script sorts the input list and finds the median using a simple formula. It handles both odd and even length lists correctly. The `sorted()` function is used to sort the list in ascending order, which is necessary for finding the median. The median is then calculated based on whether the list has an odd or even number of elements.