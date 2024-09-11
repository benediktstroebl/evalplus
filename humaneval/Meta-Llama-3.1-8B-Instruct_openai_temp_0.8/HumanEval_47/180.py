### Median Calculation Script
```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    The median is calculated by first sorting the list and then finding the middle value.
    If the list has an odd number of elements, the middle value is returned.
    If the list has an even number of elements, the average of the two middle values is returned.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """

    # Check if the list is empty
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, return the middle value
    if n % 2 == 1:
        return sorted_l[n // 2]

    # If the list has an even number of elements, return the average of the two middle values
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script calculates the median of a list of numbers by first sorting the list and then finding the middle value or the average of the two middle values, depending on whether the list has an odd or even number of elements. It also includes input validation to raise an error if the list is empty.