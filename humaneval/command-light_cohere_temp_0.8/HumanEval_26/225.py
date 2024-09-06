```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Keep only the Ventures with distinct values.
    """
    numbers
   return a new list with unique values.
    """
    test_removeself:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = [x for x in numbers if x < numbers.count(x)]
    return result
```

This function utilizes a generator expression to create a new list with unique values from the input list, ensuring no duplicates.  The function then returns this new list as the output.