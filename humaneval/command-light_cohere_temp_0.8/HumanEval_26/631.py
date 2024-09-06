```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove elements that occur more than once from a list of integers.
    Input: numbers is a list of integers.
    Return: A new list without any duplicates.
    """
"""
    new_list = [x for x in numbers if numbers.count(x) == 1]
    return new_list
```
The provided code defines a function named `remove_duplicates`, which takes a list of integers as input and returns a new list without any duplicate elements. The function employs a iterable `count` function, which returns the number of occurrences of an element in a list, to create a new list that contains only the elements from the original list that occur exactly once. The code is written in a clear and concise manner, and follows the best practices of Python programming.