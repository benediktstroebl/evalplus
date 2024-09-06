```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i == numbers[i][::-1][0]]
def test_rolling_max() -> None:
    numbers = [1, 2, 3, 2, 3, 4, 2]
    expected = [1, 2, 3, 3, 3, 4, 4]
    actual = rolling_max(numbers)
    assert expected == actual, "Failed test: Rolling maximum is not calculated correctly."
```