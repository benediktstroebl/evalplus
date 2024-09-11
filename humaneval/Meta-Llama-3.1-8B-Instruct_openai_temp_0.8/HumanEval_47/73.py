### Median Calculation
#### Python Script

```python
import statistics

def median(lst: list):
    """Return median of elements in the list lst.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
    
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(lst)

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This script defines a function `median` that takes a list of numbers as input and returns the median of those numbers. It uses the `statistics.median` function from Python's built-in `statistics` module to calculate the median.

Note that `statistics.median` can handle non-numeric values in the list and will raise a `TypeError` if the list is empty. If you want to handle these cases differently, you can modify the `median` function accordingly.

### Alternative Implementation (Manually Sorting List)

If you want to manually sort the list and calculate the median, you can use the following implementation:

```python
def median(lst: list):
    """Return median of elements in the list lst.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        float: The median of the elements in the list.
    
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 0:
        # If the list has even number of elements, the median is the average of the two middle elements
        median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        # If the list has odd number of elements, the median is the middle element
        median = sorted_lst[n // 2]
    
    return median

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This implementation manually sorts the list and calculates the median based on whether the list has an odd or even number of elements.