```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Sample test cases
test_sum_product = [
    [1, 2, 3, 4],
    [],
    [5, 6, 7],
    [10, 20, 30],
]

for test in test_sum_product:
    actual = sum_product(test)
    assert actual == (sum(test), product(test)), "Error in sum_product function"
```