### Calculating the Median of a List
#### Median Function Implementation

```python
def median(l: list) -> float:
    """
    Return the median of elements in the list l.
    
    The median is the middle value in a sorted list of numbers. 
    It is the 50th percentile if the list has an odd number of elements. 
    If the list has an even number of elements, the median is the average of the two middle values.

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
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return sorted_list[n // 2]
    
    # If the list has an even number of elements, return the average of the two middle values
    else:
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then checks if the list has an odd or even number of elements. If it's odd, it returns the middle value. If it's even, it returns the average of the two middle values. The function is then tested with some example lists to demonstrate its usage.