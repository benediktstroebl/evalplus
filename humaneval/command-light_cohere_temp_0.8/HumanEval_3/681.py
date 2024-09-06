```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test cases
operations_test = [
    [1, 2, -4, 5],
    [-10, 20, -5],
    [-11, 22, -1]
]

print(below_zero(operations_test))  # Prints True

operations_double = [10, 20, -5]
print(below_zero(operations_double))  # Prints True

operations_negative = [-10, 20, -5]
print(below_zero(operations_negative))  # Prints True

```
This code defines a function `below_zero` that takes a list of operations as an argument and checks whether any of the operations would cause a balance of the account to fall below zero. It then iterates over the scenario, for each operation it checks whether the balance goes below zero, if so it returns True. Otherwise, it returns False. 

The test cases are then run, and the output will be True for all of them, since the balance will always be non-negative after the operations are performed.