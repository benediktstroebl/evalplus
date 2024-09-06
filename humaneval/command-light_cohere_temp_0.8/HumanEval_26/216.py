```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    expected = [1, 3, 4]
    actual = remove_duplicates(numbers)
    assert expected == actual
test_remove_duplicates()
``` 
This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes duplicate elements. The function uses a set to keep track of seen numbers and a list to store unique numbers. The function then loops through the numbers and adds any not previously seen numbers to the result list and the set.