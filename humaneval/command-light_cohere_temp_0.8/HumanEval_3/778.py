Here is a self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, 
    and at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, 3]
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```
The above code checks a list of deposit and withdrawal operations to determine if the balance falls below zero at any point. The function iterates through each operation in the list and adds it to the running balance. If the balance falls below zero, the function returns True; otherwise, it returns False.