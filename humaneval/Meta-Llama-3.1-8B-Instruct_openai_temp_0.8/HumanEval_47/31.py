```python
def median(l: list) -> float:
    """Return median of elements in the list l.
    
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
    sorted_l = sorted(l)
    length = len(sorted_l)
    if length % 2 == 1:
        # If the length of the list is odd, the median is the middle element
        return sorted_l[length // 2]
    else:
        # If the length of the list is even, the median is the average of the two middle elements
        mid1 = sorted_l[length // 2 - 1]
        mid2 = sorted_l[length // 2]
        return (mid1 + mid2) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This Python script defines a function `median` that calculates the median of a list of numbers. It first sorts the list, then checks if the length of the list is odd or even. If it's odd, the median is the middle element. If it's even, the median is the average of the two middle elements. The example usage demonstrates how to use this function to calculate the median of different lists.