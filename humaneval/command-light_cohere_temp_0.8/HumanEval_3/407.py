Here's the self-contained Python script that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    
    # Check through below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
```
This script defines a function `below_zero` that takes a list of integers `operations` as input. The function initializes a balance of 0. Then, it loops through each operation in the list. If the current balance falls below 0, it returns True, otherwise, adds the operation to the balance and continues. If the loop ends, the function returns False, indicating that the balance never fell below zero.