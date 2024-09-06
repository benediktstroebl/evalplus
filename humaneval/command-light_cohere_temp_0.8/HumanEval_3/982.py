Here is the self-contained Python script with the below_zero function that solves the problem of detecting if the balance of a bank account ever falls below zero:
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

This function iterates through the list of operations and for each operation, it subtracts the operation from the balance. The function returns True if the balance ever falls below zero, and False otherwise.