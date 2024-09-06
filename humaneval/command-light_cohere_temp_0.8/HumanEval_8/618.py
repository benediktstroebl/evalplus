```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
assert isinstance(result, Tuple)
assert len(result) == 2
assert 0 <= result[0] < 4
assert result[0] == sum(numbers)
assert result[1] == numbers[0] * numbers[1]
```