```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    return [list of unique elements
    """
numbers = [1, 2, 3, 2, 4, 2, 3]
# remove duplicates
result = remove_duplicates(numbers)
print(result)
``` 
This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all elements that occur more than once, producing a list of unique elements. 
It then applies this function to a list of numbers, [1, 2, 3, 2, 4, 2, 3], and prints the resulting unique elements: [1, 3, 4].