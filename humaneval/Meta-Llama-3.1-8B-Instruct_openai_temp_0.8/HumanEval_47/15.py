```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_l = sorted(l)
    length = len(sorted_l)

    # Handle the case where the list has an odd number of elements
    if length % 2 == 1:
        return sorted_l[length // 2]

    # Handle the case where the list has an even number of elements
    else:
        mid1 = sorted_l[length // 2 - 1]
        mid2 = sorted_l[length // 2]
        return (mid1 + mid2) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list, and then checks if the length of the list is odd or even. If the length is odd, it returns the middle element. If the length is even, it returns the average of the two middle elements. The script includes two test cases to demonstrate the function's correctness.