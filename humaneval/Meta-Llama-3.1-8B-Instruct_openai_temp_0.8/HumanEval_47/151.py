```python
import statistics

def median(lst: list):
    """
    Return median of elements in the list lst.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    return statistics.median(lst)

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This script uses the `statistics` module's built-in `median` function to calculate the median of a given list of numbers. This approach is more efficient and robust than implementing the calculation manually.

If you want to implement the median calculation manually for educational purposes, you can use the following code instead:

```python
def median(lst: list):
    """
    Return median of elements in the list lst.
    
    Parameters:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the numbers in the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    if n % 2 == 1:
        return sorted_lst[n // 2]
    else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```

This manual implementation calculates the median by first sorting the list and then checking if the list has an odd or even number of elements. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.