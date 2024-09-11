### Median Calculator
#### Python Function to Calculate the Median of a List

```python
def median(l: list):
    """
    Return median of elements in the list l.

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
    # Sort the list in ascending order
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements, the median is the middle element
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, the median is the average of the two middle elements
    else:
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script defines a function `median` that calculates the median of a list of numbers. It first sorts the list in ascending order, then checks if the list has an odd or even number of elements. If it has an odd number of elements, the median is the middle element. If it has an even number of elements, the median is the average of the two middle elements. The function is tested with the provided examples.