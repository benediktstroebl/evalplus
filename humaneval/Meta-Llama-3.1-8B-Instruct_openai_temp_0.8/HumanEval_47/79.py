```python
def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in an ordered integer list. If the list has an even number of elements, the median is the average of the two middle values.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the list.

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

    # If the list has an odd number of elements, return the middle value
    if n % 2!= 0:
        return sorted_l[n // 2]
    # If the list has an even number of elements, return the average of the two middle values
    else:
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

However, if the list has a large number of elements or is very large, sorting the list can be inefficient. In such cases, you can use a different approach to find the median. This approach involves using the `numpy` library to efficiently find the median.

Here is the updated code:

```python
import numpy as np

def median(l: list):
    """
    Return median of elements in the list l.

    The median is the middle value in an ordered integer list. If the list has an even number of elements, the median is the average of the two middle values.

    Args:
    l (list): A list of numbers.

    Returns:
    float: The median of the list.

    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Convert the list to a numpy array
    arr = np.array(l)

    # Return the median of the array
    return np.median(arr)


# Test the function
print(median([3, 1, 2, 4, 5]))  # Expected output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected output: 15.0
```

This updated code uses the `np.median` function from the `numpy` library, which is much faster than sorting the list for large inputs.