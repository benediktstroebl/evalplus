```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = sum(numbers) * product(numbers)
    assert result == (0, 1), "Empty sum should be 0 and empty product should be 1"
    assert len(numbers) > 0, "List should not be empty"
    assert result % 2 == 0, "Sum should be even"
    return result
```