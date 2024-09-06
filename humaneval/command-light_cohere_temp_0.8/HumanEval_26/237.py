```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements from left as in the input."""
    return [i for i in numbers if i < numbers.count(i)]
``` 
This function uses a list comprehension to create a new list that contains only the unique elements from the input list.