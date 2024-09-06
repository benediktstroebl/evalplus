```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in zip(numbers, numbers[1:])][::-1] if idx < len(numbers) and numbers[idx] > numbers[idx + 1]
def test_rolling_max(numbers: List[int]) -> None:
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 3, 4, 4], "Passing test 1"
    assert rolling_max([10, 20, 30, 10, 40]) == [10, 20, 30, 40, 40], "Passing test 2"
    assert rolling_max([]) == [], "Passing test 3"
    assert rolling_max([4, 2, 4, 3]) == [4, 4, 4], "Passing test 4"
numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max(numbers)
```