Here's the complete Python script with self-contained function `below_zero` that checks whether the balance of the account ever falls below zero in a list of deposit and withdrawal operations: 
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```

This `below_zero` function takes a list of integers as an argument, representing deposit and withdrawal operations. The function initializes a balance to 0, and then iterates through each operation in the list. For each operation, it checks whether the balance goes below 0. If it finds a balance goes negative, it returns `True`. Otherwise, the function returns `False` after processing all operations.