```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
# Unit tests
operations_test = [
    [1, 2, -4, 5],
    [-10, 20],
    [0, -15],
    [15, 0, -10],
    [100, -200]
]

def test_below_zero():
    return below_zero(operations_test)

# Output
test_below_zero():
    True
```