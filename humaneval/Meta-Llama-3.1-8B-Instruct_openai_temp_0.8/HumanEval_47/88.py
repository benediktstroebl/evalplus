### Median Calculation in Python
#### A Self-Contained Script

```python
def median(lst: list) -> float:
    """Return median of elements in the list lst.

    Args:
        lst: A list of numbers.

    Returns:
        The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # If n is odd, the median is the middle element
    if n % 2!= 0:
        return sorted_lst[n // 2]
    
    # If n is even, the median is the average of the two middle elements
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2

# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script takes a list of numbers and calculates the median. If the list has an odd length, it returns the middle element. If the list has an even length, it returns the average of the two middle elements. It includes example usage at the end to demonstrate its functionality.