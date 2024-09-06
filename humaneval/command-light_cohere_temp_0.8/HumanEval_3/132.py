Here is the complete Python script that implements the function `below_zero` from the prompt:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```

The function checks if the balance of the account goes below zero at any point during the loop and returns True if this is the case, and False otherwise. It starts with an initial balance of 0 and adds each operation in the list. If the balance goes below zero at any point, the function returns True; otherwise, it returns False.