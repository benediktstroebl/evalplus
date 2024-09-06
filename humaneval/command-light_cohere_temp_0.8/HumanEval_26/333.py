```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from a list of integers.
    Keep only the partnership once.
    Return a duplicates removed list.
    """
   
    array will be returned
    """
    return [num for num in numbers if numbers.count(num) != 1]
```
The provided code defines a Python function named remove_duplicates that takes a list of integers as input and produces a new list with duplicate elements removed. The function utilizes the `count()` to determine if a number is duplicated in the input list and removes the duplicate occurrences, then returns the array with unique elements.