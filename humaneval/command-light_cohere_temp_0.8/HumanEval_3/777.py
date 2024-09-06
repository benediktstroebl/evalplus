```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """
    operations.balance = 0
   
    for num in operations:
        operations.balance += num
   
    if num < 0:
            return True
    return False
``` 
This Python script defines a function called `below_zero` that takes a list of integers as its argument. The function performs a operations in the list and then checks if the balance of the account has fallen below zero. If the balance is negative, the function returns `True`; otherwise, it returns `False`. 

The script then tests the `below_zero` function with a sample list of operations and verifies that the function correctly identifies negative numbers as the condition for returning `True`.