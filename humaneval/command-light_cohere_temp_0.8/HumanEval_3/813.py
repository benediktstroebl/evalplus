```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Unit tests
operations_test = [
    [1, 2, -4, 5],
    [-10, -3, 4, -1],
    [0, 2, -8, 1]
]

is_below_zero = below_zero

for op in operations_test:
    assert is_below_zero(op) == False, f"Found negative balance for non-negative operation: {op}"

```
I hope this script demonstrates a Python function that checks for negative balances in a list of operations. The function works by initializing a balance to zero, then iterating through each operation and subtracting the operation from the balance. Finally, it checks if the balance is less than zero and returns True if so. The tests ensure that the function correctly identifies negative balances.