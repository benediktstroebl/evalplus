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

This script defines a function called `below_zero` that takes in a list of integer operations, representing deposits and withdrawals, on a bank account. The function initializes the balance to 0 and then iterates through each operation in the input list.

For each operation, it adds it to the current balance. If at any point the calculated balance falls below 0 (indicating a negative balance), the function immediately returns `True`, indicating that the account balance fell below zero at least once. If no negative balance is encountered, it returns `False` at the end of the loop when all operations have been processed.

The function returns `False` if the account balance never falls below zero, and `True` otherwise. This functionality is illustrated through example in the docstring, as required.