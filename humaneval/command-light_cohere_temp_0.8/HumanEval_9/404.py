```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((i, num) for num, i in zip(numbers, range(len(numbers)))) if i != numbers[i]]
def test_rolling_max(numbers):
    assert rolling_max(numbers) == [num for num in numbers if num == max(numbers) or num in numbers[1:]]
    assert rolling_max([1, 2, 3]) == [1, 2, 3]
    assert rolling_max([100, 200, 150]) == [100, 150]
    assert rolling_max([10, 20, 30]) == [10, 30]
```