```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 0:  # If the list has an even number of elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2
    else:  # If the list has an odd number of elements
        return sorted_list[n // 2]

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order. If the list has an even number of elements, it returns the average of the two middle elements. If the list has an odd number of elements, it returns the middle element. The function includes docstrings to provide documentation and example usage to demonstrate how to use the function.