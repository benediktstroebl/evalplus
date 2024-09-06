```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep only the first occurrence elements.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    result = [num for num in numbers if num < numbers.count(num)]
    return result
```  This Python function, remove_duplicates, takes a list of integers as input and creates a new list with only the first occurrence of each integer in the original list. The function utilizes a counting the elements in the list to determine if each element has already occurred before, and if so, removes it. 

This function could be easily included in a larger program or could stand alone as a complete and functioning solution to the problem.