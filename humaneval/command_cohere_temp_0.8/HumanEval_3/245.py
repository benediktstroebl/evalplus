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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or a withdrawal). The function simulates the effects of these operations on a bank account starting with a balance of 0. It iterates through each operation in the input list and updates the balance accordingly. If at any point the balance falls below 0 (indicating a negative balance), it immediately returns `True`. If none of the operations cause the balance to go negative, it returns `False` at the end. 

This solution follows the given test examples provided in the prompt and will return `False` for the first case and `True` for the second case.