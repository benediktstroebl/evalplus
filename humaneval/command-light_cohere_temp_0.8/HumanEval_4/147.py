Here's the code:
```python
from typing import List

def mean_absolute_deviation(numbers):
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset
    
    Mean Absolute Deviation = average | x - mean | 

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4]) 
    """2.0 == 20/2.0 + 3.0 + 1.0) 

   0.0
    - 1.0)

    # List is not iterable, so we pass each number 
    individually using the list comprehension
    """
    return float(numbers[-1] - numbers[0])

# Test case
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0)

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0)
print(mean_absolute_deviation([1.0, 2, 3, 4]) == 2.0)
```