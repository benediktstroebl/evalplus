```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling max elements from the given list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
   >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4]
    """
    return [x for x, i in zip(numbers, numbers[1:])][::-1]]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print("Test 1: ", rolling_max(numbers))

numbers = [1, 2, 3, 4, 2, 3, 5]
print("Test 2: ", rolling_max(numbers))

numbers = [1, 2, 3, 4, 5, 6]
print("Test 3: ", rolling_max(numbers))
```

This Python script defines a function called `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The `numbers` list is passed as an argument to the function, and the function returns a new list containing the rolling maximum elements. 

The script then tests the function with three different sets of numbers and prints out the resulting lists of rolling maximum elements.