Here's the Python script to solve the issue in a markdown code block:

```python
def median(l: list):
    """
    Return median of elements in the list l.
    
    If the list has an odd number of elements, the median is the middle value.
    If the list has an even number of elements, the median is the average of the two middle values.

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

    # Sort the list
    sorted_l = sorted(l)

    # Get the length of the list
    n = len(sorted_l)

    # If the list has an odd number of elements
    if n % 2!= 0:
        # The median is the middle value
        return sorted_l[n // 2]
    else:
        # The median is the average of the two middle values
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))
print(median([-10, 4, 6, 1000, 10, 20]))
```

This script first sorts the input list using the built-in `sorted` function. It then determines whether the list has an odd or even number of elements. If the list has an odd number of elements, it returns the middle value. If the list has an even number of elements, it returns the average of the two middle values.