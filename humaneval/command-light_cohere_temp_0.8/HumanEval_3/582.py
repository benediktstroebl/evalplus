```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

This function will return True if the balance ever falls below zero, and False otherwise.  It uses a balance variable to keep track of the account balance, and loops through the operations.