### Median Calculator Script
```python
def median(l: list):
    """Return median of elements in the list l.
    
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
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:
        # If the length of the list is even, return the average of the two middle numbers
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the length of the list is odd, return the middle number
        return sorted_l[n // 2]


# Example usage:
print(median([3, 1, 2, 4, 5]))  # 3
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0
```
This script defines a function `median` that calculates the median of a given list of numbers. It first sorts the list, then checks whether the length of the list is even or odd. If it's even, it returns the average of the two middle numbers. If it's odd, it returns the middle number. The script includes example usage to demonstrate its functionality.