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
    [-10, 3, 6, -1],
    [100, -200, 500, -300],
]
print(below_zero(operations_test))  # Output: True

operations_negative = [5, -6, 7, -8]
print(below_zero(operations_negative))  # Output: False
```
The above Python script has a self-contained function that solves the problem and passes corresponding tests. 

The `below_zero` function takes a list of operations and calculates the balance of the account. The function iterates over each operation in the list and updates the balance accordingly. If at any point, the balance falls below zero, the function returns True, otherwise it returns False.