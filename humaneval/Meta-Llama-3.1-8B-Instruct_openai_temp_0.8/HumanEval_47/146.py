### Median Calculation in Python
#### A self-contained script to calculate the median of a list of numbers.

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    The median is calculated by first sorting the list in ascending order. 
    If the list has an odd number of elements, the median is the middle element.
    If the list has an even number of elements, the median is the average of the two middle elements.

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
    sorted_l = sorted(l)
    n = len(sorted_l)

    # Calculate the middle index
    mid = n // 2

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_l[mid]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        return (sorted_l[mid - 1] + sorted_l[mid]) / 2


# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script first sorts the input list in ascending order, and then calculates the median based on whether the list has an odd or even number of elements. The median is then returned as a float.