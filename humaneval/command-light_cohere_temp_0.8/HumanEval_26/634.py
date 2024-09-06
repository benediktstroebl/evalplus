```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements from left as is in the input.
    """
    return [list(set(numbers))
    """
    return numbers[:]
``` 
This function removes duplicate values from a list of integers and returns the modified list. 

It uses the set() function to create a set of the input list values and the [] slicing syntax to return only unique values from the original list.