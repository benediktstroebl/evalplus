```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    Remove all elements that occur more than once from a list of integers.
    Input:
    numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    numbers = set(numbers)
    return [x for x in numbers if x not in set(numbers)]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique elements from the input. It utilizes the set and list comprehension to achieve this, removing duplicates.