### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        float: The median of the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Calculate the length of the list
    n = len(sorted_l)
    
    # Check if the list is empty
    if n == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # If the list has an odd number of elements, the median is the middle element
    elif n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```