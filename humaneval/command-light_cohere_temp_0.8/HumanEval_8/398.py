```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1] + sum_product(numbers[1:])
    return (result, result * numbers[0])

# Unit tests
test_sum_product = [
    "def test_sum_product():
        assert sum_product([1, 2]) == (2, 2)
        assert sum_product([]) == (0, 1)
        assert sum_product([1, 2, 3]) == (6, 12)
        assert sum_product([1, 2, 3, 4]) == (10, 24)
]
```