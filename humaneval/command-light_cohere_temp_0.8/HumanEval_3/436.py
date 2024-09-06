```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            balance += operation
    return balance < 0
```
This code defines a function below_zero that checks whether the balance of a bank account starts with zero falls below zero after processing a list of deposit and withdrawal operations. The function iterates through operations in the list, and if any operation is a negative value, it subtracts that operation from the balance. If the balance after the operation is a positive value, it adds that operation to the balance.