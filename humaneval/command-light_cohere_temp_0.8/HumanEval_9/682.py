```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), range(len(numbers))) if numbers[idx] > numbers[(idx - 1) % len(numbers)]]
def test_rolling_max(numbers: List[int]) -> None:
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 3, 4, 4], "Test 1 failed"
    assert rolling_max([10, 2, 3, 5, 4, 3, 2, 1, 6]) == [10, 3, 5, 4, 6], "Test 2 failed"
numbers = [10, 2, 3, 5, 4, 3, 2, 1]
test_rolling_max(numbers)
print("All tests passed")
```