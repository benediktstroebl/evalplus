```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
```
This code provides a remove_duplicates function that takes a list of integers and returns a new list with duplicates removed. It uses a all elements are the same in the input list and the order is preserved. The test_remove_duplicates function tests the remove_duplicates function by passing a list of integers and asserts that the result is as expected.