```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.rolling_max() = numbers[::-1][1:] + [max(numbers[0], numbers[-1])] + numbers[:-1]
    return numbers[1:] + rolling_max([2, 3, 4])
def test_rolling_max() -> None:
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max(numbers)
    assert result == [1, 2, 3, 3, 3, 4, 4]
    numbers = [1, 3, 2, 4, 5]
    result = rolling_max(numbers)
    assert result == [1, 3, 4, 5]
```