```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.find_duplicates(seen, numbers) ]


def find_duplicates(set_seen, numbers: List[int]) -> List[int]:
    return [x for x in numbers if x in set_seen and x in numbers[numbers] and (x, set_seen.find_duplicates(set_seen, numbers))]

numbers = [1, 2, 3, 2, 4]
set_seen = set()
print(remove_duplicates(numbers))
print(find_duplicates(set_seen, numbers))
``` 
This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list of integers without any duplicates. The function uses a set to keep track of seen integers, and the input list is looped through to check if each element is not in the set and not already in the input list. The `find_duplicates` function is also defined and returns a list of integers that appear in the set more than once and are also in the input list.