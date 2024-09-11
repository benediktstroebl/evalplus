### Median Calculator
#### Purpose
This script calculates the median of a given list of numbers.

#### Code
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
    
    # Check if the list is empty
    if len(l) == 0:
        raise ValueError("Cannot calculate median of an empty list")
    
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the length is even, the median is the average of the two middle numbers
    if n % 2 == 0:
        median = (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    # If the length is odd, the median is the middle number
    else:
        median = sorted_l[n // 2]
    
    return median

# Example usage:
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

#### Explanation
This script defines a function `median` that takes a list of numbers as input and returns the median. It first checks if the list is empty and raises a `ValueError` if it is. Then it sorts the list in ascending order. The median is calculated as follows:

* If the length of the list is even, the median is the average of the two middle numbers.
* If the length of the list is odd, the median is the middle number.

The script then demonstrates the usage of the `median` function with two example lists.