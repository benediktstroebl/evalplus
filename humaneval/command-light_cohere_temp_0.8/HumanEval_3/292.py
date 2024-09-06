```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    """
return balance < 0 || sum(op) < 0
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
``` 
This function below_zero takes a list of operations as input and returns a boolean value that indicates whether the balance of the account falls below zero. The function uses a balance variable to keep track of the current balance and iterates over each operation in the input list. If the balance becomes below zero, the function returns True, otherwise it returns False.