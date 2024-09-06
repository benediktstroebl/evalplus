```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """ 
    Check whether the balance of the account ever falls below zero. 
    using a single integer deposit and withdrawal operations provided.
    
    If balance = 0 
    for operation in operations:
        balance = balance + operation
        if balance < 0: 
            return True 
    return False
```