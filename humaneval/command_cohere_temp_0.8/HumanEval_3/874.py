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

The `below_zero` function iterates through the list of `operations` and accumulates the balance of the bank account in a loop. It keeps adding the `op` (deposit or withdrawal) to the current balance. If at any point the balance goes negative, it immediately returns `True`, indicating that the balance fell below zero at least once. If the loop completes without the balance dropping below zero, it returns `False`, meaning the balance never fell below zero. 

This approach has a time complexity of O(n), where 'n' is the number of operations, making it efficient for larger lists of operations.