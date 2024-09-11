```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is calculated by sorting the list first, then finding the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the elements in the list l.
    """
    # Check if the list is empty
    if not l:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Find the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test cases
if __name__ == "__main__":
    print(median([3, 1, 2, 4, 5]))  # Output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
    try:
        print(median([]))
    except ValueError as e:
        print(e)  # Output: Cannot calculate median of an empty list
```

This script defines a function `median` that calculates the median of a list of numbers. It first checks if the list is empty, then sorts the list in ascending order. If the list has an odd number of elements, it returns the middle element. If the list has an even number of elements, it returns the average of the two middle elements. The script also includes test cases to verify the correctness of the `median` function.