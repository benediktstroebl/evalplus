### Median Function
#### Returns the median of elements in a list

```python
import statistics
import math

def median(l: list) -> float:
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Use the median function from the statistics library
    return statistics.median(l)
```

However, if you want to implement the median function from scratch, you can use the following code:

```python
def median(l: list) -> float:
    """
    Return median of elements in the list l.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")

    sorted_list = sorted(l)
    n = len(sorted_list)
    
    if n % 2 == 1:
        # If the number of elements is odd, the median is the middle element
        return sorted_list[n // 2]
    else:
        # If the number of elements is even, the median is the average of the two middle elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2
```

Both of these functions will return the median of the elements in the list. However, the first function uses the built-in `statistics.median` function, which is more concise and efficient. The second function implements the median calculation from scratch, which can be useful for educational purposes or when working in an environment without access to the `statistics` library.