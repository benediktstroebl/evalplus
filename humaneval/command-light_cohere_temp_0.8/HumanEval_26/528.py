```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num > 0]
    return result

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 5]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected
```