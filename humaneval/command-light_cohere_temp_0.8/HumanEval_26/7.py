```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   
    return result

def test_remove_duplicates(test_numbers: List[int]) -> None:
    expected = [1, 2, 3, 2, 4]
    result = remove_duplicates(test_numbers)
    assert result == expected
```