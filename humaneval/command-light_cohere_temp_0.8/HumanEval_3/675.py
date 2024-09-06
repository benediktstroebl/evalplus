Here's the Python script with a self-contained function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, and
    at that point function should return True. Otherwise, it should return False.
    """
return balance < 0 and sum(operations) < 0"""
    balance = 0
    total_amount = 0
    for amount in operations:
        balance += amount
        total_amount += amount
    return balance == 0 and total_amount < 0
```
This code defines a function called below_zero that takes a list of operations as input. The function aims to detect if the balance of the account falls below zero at any point. It does this by keeping track of the current balance and the total amount of deposits and withdrawals. The function iterates over each operation in the list and adds both the amount to the balance and the total amount. At the same point, it checks if the balance is equal to zero and the total amount of deposits and withdrawals is less than zero.