### Median of a List
#### Python Script

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
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 0:
        # If the length of the list is even
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # If the length of the list is odd
        median = sorted_l[n // 2]

    return median

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```