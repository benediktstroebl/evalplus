```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in reversed(sorted(numbers)) if num > max_rolling]
 
def test_rolling_max() -> None:
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([10, 2, 3, 1, 4]) == [10, 2, 3, 4]
    assert rolling_max([-5, -3, -4]) == [-4, -3, -4]
    assert rolling_max([10, 20, 30]) == [10, 20, 30]
```