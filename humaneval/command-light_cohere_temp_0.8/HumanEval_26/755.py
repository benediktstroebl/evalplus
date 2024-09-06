```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
    result = remove_duplicates([10, 20, 30, 10, 40, 50])
    assert result == [10, 20, 30, 50]
```