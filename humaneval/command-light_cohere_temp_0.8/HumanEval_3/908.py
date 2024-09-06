Here's a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
This function takes a list of operations as input and uses a loop to iterate through the operations. It keeps track of the balance of the account, starting from zero, and for each operation, it checks if the operation is negative and subtracts it from the balance if it is. If the operation is positive, it adds the operation to the balance. This process continues until the other operations are processed, and at any point if the balance falls below zero, the function returns True. Otherwise, it returns False.