```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers.
    numbers = [1, 2, 3, 2, 4, 2]
    return [x for x in numbers if numbers.count(x) == 1]
```
The above function takes a list of integers as input and returns a new list with all the integers only once occurring in the original list.

It utilizes a for loop and a count function to create a new list with all the integers that only occur once in the original list.