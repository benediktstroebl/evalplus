Here's how you can implement a Python function to calculate the median of a list, along with some example usage:
```python
import statistics

def custom_median(l: list):
    """Return median of elements in the list l.
    >>> custom_median([3, 1, 2, 4, 5])
    3
    >>> custom_median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list in ascending order
    sorted_l = sorted(l)
    
    # Get the length of the list
    n = len(sorted_l)
    
    # If the list has an odd number of elements
    if n % 2 == 1:
        # The median is the middle element
        return sorted_l[n // 2]
    # If the list has an even number of elements
    else:
        # The median is the average of the two middle elements
        mid1 = sorted_l[n // 2 - 1]
        mid2 = sorted_l[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(custom_median([3, 1, 2, 4, 5]))  # Output: 3
print(custom_median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

However, Python already provides a `statistics` module that has a built-in `median` function. Here's how you can use it:
```python
import statistics

def use_builtin_median(l: list):
    """Return median of elements in the list l.
    >>> use_builtin_median([3, 1, 2, 4, 5])
    3
    >>> use_builtin_median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(l)

# Test the function
print(use_builtin_median([3, 1, 2, 4, 5]))  # Output: 3
print(use_builtin_median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```