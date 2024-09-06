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
    result = remove_duplicates(numbers)
    assert len(result) == 3
    assert result == [1, 3, 4]
test_remove_duplicates()
```  This code defines a remove_duplicates function that takes a list of integers as input and returns a new list with all distinct integers from the input. The function uses a same set to keep track of the integers it has seen so far, and then appends any new integer to the result list if it hasn't been seen before. The test_remove_duplicates function tests the remove_duplicates function by passing a list of integers and checking that the resulting list has the correct number of distinct integers.