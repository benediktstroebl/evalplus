```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by first sorting the list in ascending order.
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.
    """
    # Check if the input is a list
    if not isinstance(l, list):
        raise TypeError("Input must be a list")

    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2 == 1:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median(l)` that calculates the median of a list of numbers. It first checks if the input is a list and raises a `TypeError` if it's not. It also checks if the list is empty and raises a `ValueError` if it is. It then sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. Finally, it provides example usage of the function.