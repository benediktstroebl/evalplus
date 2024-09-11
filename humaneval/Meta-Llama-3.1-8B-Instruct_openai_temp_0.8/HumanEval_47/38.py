```python
def median(l: list) -> float:
    """
    Return the median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of elements in the list l.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    # Handle even and odd length lists separately
    if n % 2 == 0:
        # For even length lists, the median is the average of the two middle numbers
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2
    else:
        # For odd length lists, the median is the middle number
        return sorted_l[n // 2]

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list, and returns the median. It handles both even and odd length lists by calculating the average of the two middle numbers for even length lists and the middle number for odd length lists. The script also provides example usage to demonstrate how to call the function.