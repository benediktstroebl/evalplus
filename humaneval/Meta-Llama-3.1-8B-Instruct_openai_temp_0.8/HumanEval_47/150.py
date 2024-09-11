### Median Calculation Script
```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
    l (list): List of numbers.

    Returns:
    float: Median of the list.

    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Check if list is empty
    if not l:
        raise ValueError("Cannot calculate median of empty list")

    # Sort the list
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If list has an odd length, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]

    # If list has an even length, return the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a function `median` that calculates the median of a list of numbers. It first checks if the list is empty and raises a `ValueError` if it is. Then, it sorts the list using the `sorted` function and calculates the median based on whether the list has an odd or even length. If the list has an odd length, it returns the middle element. If the list has an even length, it returns the average of the two middle elements. The script then tests the function with two example lists.