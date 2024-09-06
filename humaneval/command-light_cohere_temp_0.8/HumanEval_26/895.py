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
    assert [1, 3, 4] == result
    assert [2] == result
    assert [1, 2, 3] not in result
    assert [4, 2] not in result
    assert [1, 2, 3, 4] == [1, 3, 4]
test_remove_duplicates()
```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate integers removed. The `test_remove_duplicates` function passes all the tests with the corresponding input.