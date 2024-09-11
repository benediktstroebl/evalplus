### Calculating the Median of a List
Here is a Python script that solves the problem:

```python
import statistics

def median(l: list):
    """Return median of elements in the list l.

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
    return statistics.median(l)

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the built-in `statistics.median` function to calculate the median of the list. However, if you want to implement the median calculation manually, here is a version of the script that does that:

```python
def median(l: list):
    """Return median of elements in the list l.

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
    sorted_l = sorted(l)
    n = len(sorted_l)
    
    if n % 2 == 0:  # If the list has an even number of elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:  # If the list has an odd number of elements
        return sorted_l[n // 2]

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This manual implementation first sorts the list, then checks if the list has an even or odd number of elements. If it has an even number of elements, it returns the average of the two middle elements. If it has an odd number of elements, it returns the middle element.