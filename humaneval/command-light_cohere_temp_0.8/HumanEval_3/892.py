```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Testing the function
# The operations in this case are in descending order, which is valid since the balance will always be decremented
# first
operations = [5, -4, 2, 1, 3]
result = below_zero(operations)
print(result)  # Output should be True
```
This script defines a function `below_zero` that checks if the operations in an input list will cause the balance of an account to go below zero. 

The loop iterates through each operation in the list, and if the balance goes below zero, the function immediately returns `True`. Otherwise, the balance is incremented by the amount of the operation.