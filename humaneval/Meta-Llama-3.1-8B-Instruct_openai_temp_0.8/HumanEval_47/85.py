### Median Calculation Script

The following script defines a function `median` to calculate the median of a list of numbers. It uses the built-in `sorted` function to sort the list, and then finds the middle element (or the average of the two middle elements if the list has an even number of elements).

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

    # If the list has an odd number of elements, return the middle element
    if n % 2 == 1:
        return sorted_list[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input, sorts the list in ascending order, and then calculates the median. The median is the middle value in the sorted list. If the list has an even number of elements, the median is the average of the two middle values. The script includes an example usage of the `median` function.