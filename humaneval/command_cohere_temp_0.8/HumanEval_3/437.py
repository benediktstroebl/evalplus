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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It calculates the total balance of the account by summing up the operations, then iterates through each operation in the list, updating the balance after each operation. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went below zero at least once. If the loop completes without the balance dropping below zero, it returns `False`, indicating that the account never fell into a negative balance. 

This solution follows the given test examples provided in the prompt and should correctly solve the problem.