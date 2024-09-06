```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if x > numbers[-1]][:int(len(numbers) - 1)]
def test_rolling_max(numbers):
    assert rolling_max(numbers) == [x for x in sorted(numbers) if x > numbers[-1]][:int(len(numbers) - 1)], "Error in rolling_max function"
test_rolling_max([1, 2, 3, 2, 3, 4, 2])
```