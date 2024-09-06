```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(sorted(numbers), range(len(numbers))) if numbers[idx] > numbers[idx - 1]]
def test_rolling_max(numbers: List[int]) -> None:
    assert rolling_max(numbers) == [n for n in numbers if n > numbers[0]] + [n for n in numbers if n > numbers[-1]]
    assert rolling_max([]) == []
    assert rolling_max([10, 30, 20]) == [10, 30]
    assert rolling_max([15, 20, 25]) == [15, 20]
```