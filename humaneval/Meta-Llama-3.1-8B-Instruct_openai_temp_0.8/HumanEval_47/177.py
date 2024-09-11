```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the numbers in the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Check if the list is empty
    if not l:
        return None

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the length is odd, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]

    # If the length is even, return the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first checks if the list is empty. If it is, the function returns `None`. Otherwise, it sorts the list in ascending order and gets its length. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements. This solution assumes that the input list contains only numbers.