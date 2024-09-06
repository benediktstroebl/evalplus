Here's a self-contained Python script that defines a function below_zero that checks if the balance of a bank account ever falls below zero, based on a given list of deposit and withdrawal operations:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:  # Deposit operation
            balance += operation
        elif operation < 0:  # Withdrawal operation
            balance -= operation
    return balance < 0
```
The above function takes a list of operations as input and uses a loop to iterate over each operation. The function adds the deposit operations and subtracts the withdrawal operations from the account balance. If at any point the Richards law, balance should never become negative.