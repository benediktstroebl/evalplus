### Median Calculator Script
```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_list = sorted(l)
    n = len(sorted_list)

    if n % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        return sorted_list[n // 2]


# Test the function
print(median([3, 1, 2, 4, 5]))   # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```
This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then checks if the length of the list is even or odd. If the length is even, it calculates the median as the average of the two middle numbers. If the length is odd, it returns the middle number. The script also includes example use cases and test statements to verify the function's correctness.