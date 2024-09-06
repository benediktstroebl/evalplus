```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False

# Example usage:
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)

```
This code solves the problem of detecting whether the balance of a bank account starts with zero and falls below zero. It uses a example usage with operations [1, 2, -4, 5] to test the function. It outputs True as the balance after the operations becomes negative will cause the balance to fall below zero, and the function will return True.