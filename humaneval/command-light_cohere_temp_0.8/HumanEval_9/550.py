```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n,i in zip(sorted(numbers),range(len(numbers)))][i+1:]
def test_rolling_max() -> None:
    assert rolling_max([1,2,3,2,3]) == [1,2,3,3,3,4]
    assert rolling_max([10, 20, 30, 10, 20]) == [10, 20, 30, 10, 20]
    assert rolling_max([99, 44, 22, 11, 66]) == [99, 44, 22, 11]
```