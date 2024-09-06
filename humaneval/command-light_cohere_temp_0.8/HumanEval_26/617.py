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
    numbers = [1, 2, 3, 2, 4, 3, 4, 5]
    result = remove_duplicates(numbers)
    assert len(result) == 4
    assert result == [1, 3, 4]
test_remove_duplicates()
```