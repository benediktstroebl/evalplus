```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
```
This Python function, below_zero, takes a list of operations as input and determines whether the account balance will ever fall below zero. The function initializes a balance to 0 and then iterates through each operation in the list. If the balance starts to become negative, it returns True. Otherwise, it returns False.