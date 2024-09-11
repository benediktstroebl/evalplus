```python
import statistics
import random

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

# Test the function with a large list of random numbers
large_list = [random.randint(-1000, 1000) for _ in range(10000)]
print(median(large_list))  # Output: around the median of the large list
```

This script uses the `statistics` module, which is part of the standard library in Python, to calculate the median of the list. If you want to implement the median calculation manually, you can use the following code:

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
    l.sort()  # Sort the list in ascending order
    n = len(l)
    
    if n % 2 == 1:  # If the list has an odd number of elements
        return l[n // 2]  # Return the middle element
    else:  # If the list has an even number of elements
        return (l[n // 2 - 1] + l[n // 2]) / 2  # Return the average of the two middle elements
```

This code first sorts the list in ascending order, then returns the middle element if the list has an odd number of elements, and the average of the two middle elements if the list has an even number of elements.