### Median Function in Python
```python
import statistics
from typing import List

def median(numbers: List[float]) -> float:
    """
    Return median of elements in the list.
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The median of the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    return statistics.median(numbers)

# Example usage
numbers = [3, 1, 2, 4, 5]
print("Median of the list:", median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print("Median of the list:", median(numbers))
```
In this script, we leverage the built-in `statistics.median()` function from Python's standard library, which calculates the median of a list of numbers. The `median()` function takes a list of numbers as input and returns the median. Note that this function assumes the input list contains at least one element; otherwise, it may raise an error.

Alternatively, if you want to write a custom implementation of the median function without using the built-in `statistics.median()` function, you can use the following code:

```python
import numpy as np
from typing import List

def median(numbers: List[float]) -> float:
    """
    Return median of elements in the list.
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The median of the list.
    
    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        # If n is even, the median is the average of the two middle numbers
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # If n is odd, the median is the middle number
        return sorted_numbers[n // 2]

# Example usage
numbers = [3, 1, 2, 4, 5]
print("Median of the list:", median(numbers))

numbers = [-10, 4, 6, 1000, 10, 20]
print("Median of the list:", median(numbers))
```
This custom implementation first sorts the input list in ascending order. Then it checks if the length of the sorted list is even or odd. If it's even, the median is the average of the two middle numbers. If it's odd, the median is the middle number.