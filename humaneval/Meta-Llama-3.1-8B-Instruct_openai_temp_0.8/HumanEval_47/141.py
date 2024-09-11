```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by sorting the list and selecting the middle value.
    If the list has an even number of elements, the median is the average of the two middle values.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list.
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


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This script defines a function `median` that calculates and returns the median of the elements in a given list. It first checks if the list is empty and raises an error in this case. Then it sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. The script also includes test cases to demonstrate the function's correctness.