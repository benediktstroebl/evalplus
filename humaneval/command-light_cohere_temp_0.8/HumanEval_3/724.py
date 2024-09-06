```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and at that point function should return True. Otherwise, it should return False.
    
    Operations are processed in order of an account.  That are all a operations. The first one is a deposit and the last one is a withdrawal.
    """ return sum(operations) < 0
```