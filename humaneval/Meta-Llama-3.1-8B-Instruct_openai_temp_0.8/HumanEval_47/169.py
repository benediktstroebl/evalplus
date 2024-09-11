```python
import statistics

def median(lst: list) -> float:
    """Return median of elements in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the list.
    
    Examples:
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

This script uses the built-in `statistics` module in Python to calculate the median. The `statistics.median()` function takes a list of numbers as input and returns the median value. The example usage demonstrates how to use this function with different lists of numbers. 

Alternatively, if you prefer to implement the median calculation without using the `statistics` module, you can use the following script:

```python
def median(lst: list) -> float:
    """Return median of elements in the list lst.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    float: The median of the list.
    
    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 0:
        # If n is even, the median is the average of the two middle numbers
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        # If n is odd, the median is the middle number
        return sorted_lst[n // 2]

# Example usage:
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

This script first sorts the input list in ascending order. Then it checks if the length of the list is even or odd. If the length is even, it returns the average of the two middle numbers. If the length is odd, it returns the middle number.