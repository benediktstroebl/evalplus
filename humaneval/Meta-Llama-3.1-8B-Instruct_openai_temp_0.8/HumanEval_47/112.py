### Median Calculator in Python
```python
def median(l: list):
    """Return median of elements in the list l.

    Args:
        l (list): List of numbers.

    Returns:
        float: Median of the numbers in the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Check if input is a list
    if not isinstance(l, list):
        raise TypeError("Input must be a list.")

    # Check if list is empty
    if len(l) == 0:
        raise ValueError("List cannot be empty.")

    # Check if all elements in the list are numbers
    if not all(isinstance(x, (int, float)) for x in l):
        raise ValueError("All elements in the list must be numbers.")

    # Sort the list in ascending order
    l.sort()

    # Get the length of the list
    n = len(l)

    # If the length of the list is odd, return the middle element
    if n % 2!= 0:
        return l[n // 2]
    # If the length of the list is even, return the average of the two middle elements
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```
This script defines a function `median` that takes a list of numbers as input and returns the median of these numbers. The median is the middle value in a sorted list of numbers. If the list has an even number of elements, the median is the average of the two middle elements. The script includes error checking to ensure that the input is a non-empty list of numbers.