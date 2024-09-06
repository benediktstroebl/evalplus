Here's the self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
This function takes a list of operations, where each operation is an integer representing a deposit or withdrawal. It iterates through loop over each operation and decrements the balance accordingly. If at any point, the balance falls below zero, the function returns True, indicating that the account balance has gone below zero. If the loop completes without any such balance going negative, the function returns False, indicating that the account balance is still valid.