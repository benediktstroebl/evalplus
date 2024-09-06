```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.max = max(numbers)
    current = numbers[0]
    rolling_max.push(current)
    current = numbers[0]
    for num in numbers[1:]:
        current = max(num, current)
        rolling_max.append(current)
    return rolling_max

def test_rolling_max():
    numbers = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max(numbers)
    assert result == [1, 2, 3, 3, 3, 4, 4]
    assert len(result) == 7
    assert sorted(result) == [max(numbers)] * 4
```