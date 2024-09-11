```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length of the list is odd, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    
    # If the length of the list is even, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the input list in ascending order. It then checks whether the length of the list is odd or even. If it's odd, the median is the middle element. If it's even, the median is the average of the two middle elements. This approach ensures that the median is always calculated correctly.