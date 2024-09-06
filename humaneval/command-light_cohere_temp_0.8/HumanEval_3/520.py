```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0: balance += operation
        elif operation < 0: balance -= operation
    return balance < 0
``` 
This code defines a function called below_zero, which takes a list of operations and checks whether the balance of the account falls below zero. The function iterates through each operation in the list, and if the operation is greater than zero, it adds it to the balance. If the operation is negative, it subtracts it from the balance. The function returns true if the balance is less than zero, and false otherwise.