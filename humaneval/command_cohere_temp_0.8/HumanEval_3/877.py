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

The code defines a function `below_zero` that takes a list of operations `List[int]` as an argument. It iterates through each operation in the list and simulates the effect of that operation on a bank account balance. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went below zero at least once. If the balance never falls below zero after processing all operations, it returns `False`. 

This solution effectively checks the balance after each operation and returns the desired boolean value without the need for an additional helper function.