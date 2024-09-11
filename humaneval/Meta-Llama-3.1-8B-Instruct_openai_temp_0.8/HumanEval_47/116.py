### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by sorting the list and selecting the middle element.
    If the list has an even number of elements, the median is the mean of the two middle elements.

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

    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle element
        return sorted_list[n // 2]
    else:
        # If the list has an even number of elements, return the mean of the two middle elements
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the built-in `sorted` function to sort the list and then calculates the median based on whether the list has an odd or even number of elements. If the list has an even number of elements, it returns the mean of the two middle elements. The script includes example usage and docstrings to explain the function's behavior.