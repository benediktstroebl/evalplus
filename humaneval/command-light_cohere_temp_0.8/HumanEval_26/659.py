```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()]]


test_remove_duplicates = [
    [1, 2, 3, 2, 4],
    [5, 6, 7, 8, 9, 8],
    [10, 1, 2, 3]
]

result = remove_duplicates(test_remove_duplicates)
print(result)
``` 
This code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate values removed. The seen set keeps track of elements that have already been encountered, and the function returns elements that are not in the seen set and not in the input keys list.