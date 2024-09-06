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

The `below_zero` function iterates through the list of `operations` and accumulates the balance of the bank account with each operation. If at any point the balance falls below zero, it immediately returns `True`. If the loop completes without the balance dropping below zero, it returns `False`. This approach ensures that the function returns the correct output for the given test cases and adheres to the requirement of detecting when the account balance falls below zero.