```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.len = len(numbers)
    result = [num for num in numbers]
    max_index = result.indexmax()
    verf rolling_max([1, 2, 3, 2, 3, 4, 2])
    assert len(result) == len(rolling_max([1, 2, 3, 2, 3, 4, 2])), "List lengths don't match!"
    assert max_index == 4, "Wrong maximum index"
    assert result[4] == 4, "Wrong maximum value"
    return result
```