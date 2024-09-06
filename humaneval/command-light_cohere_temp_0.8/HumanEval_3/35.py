```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with 
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise it should return False."""
    if any([x < 0 for x in operations]):
        return True
    else:
        return False
``` 
This code defines a function `below_zero` that takes a list of integers `operations` as input and returns a boolean value `True` if any operation in the list would cause the balance of the account to fall below zero, and `False` otherwise. 
This function uses the list comprehension and the any() function to check if there are any operations in the list that would cause a negative balance. 

You can use this function to solve the problem and pass tests by calling the function with a list of test operations and verifying the returned value.