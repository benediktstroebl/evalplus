```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < numbers.count(num)]
def test_remove_duplicates(numbers: List[int]) -> None:
    expected = [1, 3, 4]
    actual = remove_duplicates(numbers)
    assert expected == actual
```