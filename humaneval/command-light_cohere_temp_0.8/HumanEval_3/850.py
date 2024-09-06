```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
            return True
    return False
``` 
The function checks if the balance falls below zero after adding all the operations. It iterates through operations and adds each operation to the balance. The function returns True if the balance is less than zero, and False otherwise.