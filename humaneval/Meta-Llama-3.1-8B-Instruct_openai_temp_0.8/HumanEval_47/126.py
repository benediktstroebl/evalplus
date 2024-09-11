```python
def median(l: list):
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.
    """
    # Check if the list is empty
    if not l:
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


# Test the function
if __name__ == "__main__":
    print(median([3, 1, 2, 4, 5]))  # Expected output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
    try:
        print(median([]))  # Expected output: ValueError
    except ValueError as e:
        print(e)  # Expected output: Cannot calculate median of an empty list
```

This script defines a function `median` that takes a list of numbers as input and returns the median of the list. The function first checks if the list is empty, in which case it raises a `ValueError`. It then sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. Finally, it tests the function with the provided test cases.