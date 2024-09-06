```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, 3]
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This script defines a function `below_zero` that checks if the operations on a bank account lead to a balance below zero, returning `True` if the balance becomes negative and `False` if it remains non-negative.   The function uses the Python's built-in `List` type and a simple loop to iterate through the operations. It initializes a `balance` to 0, and then iterates through each operation in the `operations` list, adding the operation to the balance. After iterating through operations, the function returns `True` if the balance is less than zero, and `False` otherwise.