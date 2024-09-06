```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False

# Unit tests
test_below_zero = [
    ( [1, 2, -4, 5], True)
, ("[]", False)
, ("[1, -1, 2]", True)
, ([0, 2, -4, 5], False)
, ([-1, 2, -5, 6], True)
]

for act, should_pass in test_below_zero:
    assert below_zero(act) == should_pass
```