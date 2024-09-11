### Median Calculator
#### A Python Script to Calculate the Median of a List of Numbers
```python
def median(l: list):
    """Return median of elements in the list l.

    The median is the middle number in a sorted list of numbers.
    If the list has an even number of elements, the median is the average of the two middle numbers.

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
    sorted_l = sorted(l)  # Sort the list in ascending order
    n = len(sorted_l)  # Get the number of elements in the list

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]

    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the list. The median is calculated by first sorting the list in ascending order, then checking if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements. The script includes example usage to demonstrate how to use the `median` function.