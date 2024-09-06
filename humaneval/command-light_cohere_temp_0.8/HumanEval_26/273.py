```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements as firsts
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [x for x in numbers if not in numbers[:-len(numbers)]]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
``` 
This function, named **remove_duplicates**, takes a list of integers as input and aims to remove any duplicate elements. It utilizes a particular list comprehension technique to filter out elements that appear more than once in the input list.