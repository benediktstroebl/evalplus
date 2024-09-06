Here's the Python script with a self-contained function that solves the problem of detecting if the balance of a bank account ever falls below zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False

# Unit tests
tests = [
    [
        [ [1, 2, -4, 5],
         [-100, 200, -999, 500]],
        [0, 100, 200]
    ]
)

for test_set in tests:
    for op in test_set:
        if below_zero(op):
            print("YES")
    else:
        print("NO")
```
This script defines a function below_zero that takes a list of operations and detects if any of them would cause the balance of the account to fall below zero. It uses a operations are added to the balance variable, and if any of them cause the balance to go below zero, it returns True. Otherwise, it returns False.