Here's a self-contained Python function that detects if the balance of a bank account ever falls below zero, and passes the tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
```
This function uses a loop to iterate over each operation in the list, and accumulates the operations to calculate the balance. It will return True if at any point, the balance falls below zero, and False otherwise.