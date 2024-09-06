```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert len(result) == 3
    assert result == [1, 3, 4]


# Test the function
test_remove_duplicates()
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The `test_remove_duplicates` function is a standalone unit test that validates the correctness of the `remove_duplicates` function by passing it a known input and checking the output against a specific assertion.