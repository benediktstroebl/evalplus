```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

This script defines a function `below_zero` that takes in a list of `operations` (of type `List[int]`), which represent the sequence of deposit and withdrawal operations on a bank account. The function initializes the balance to 0 and then iterates through each operation in the list. It updates the balance accordingly by adding to it for deposits and subtracting from it for withdrawals.

Then, during this iteration, if the balance ever falls below zero (i.e., if `balance < 0`), the function immediately returns `True`, indicating that the account balance fell below zero at some point during the operations. If the balance never falls below zero, the function continues through the entire list and returns `False` at the end, indicating that the account never fell into a negative balance. 

The docstring exemplifies the function's behavior with a couple of test cases, showcasing how the function correctly detects when the balance falls below zero and returns `True` in those cases.