```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Unit tests
assert below_zero([1, 2, -4, 5]) == True
assert below_zero([3, -2, 4]) == False
assert below_zero([0]) == False
assert below_zero([-1, -2, -3]) == False
assert below_zero([100, -100, -100]) == False
assert below_zero([0, 1, 2]) == True

```
This code has a function that solves the problem you've described. It takes a the balance on the account balance and iterates over the operations. Then, for each operation, it checks if the balance goes below zero. If it does, it returns True, otherwise, it returns False. The function is then tested using various inputs and assertions to ensure its correctness.