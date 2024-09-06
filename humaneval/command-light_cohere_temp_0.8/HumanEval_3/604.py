```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
# Unit test
test_cases = [
    [ below_zero([1, 2, -4, 5]) ], False),
    [below_zero([1, 2, 3]) ], True),
    [below_zero([10, 20, 30]) ], False),
    [below_zero([-1, 2, -3]) ], True),
    [below_zero([0]) ], False),
    [below_zero([100, 200, 300]) ], False
]

for _,y in test_cases:
    assert below_zero(y) == _y
```