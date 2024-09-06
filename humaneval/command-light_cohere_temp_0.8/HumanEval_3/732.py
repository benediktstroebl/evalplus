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
The balance variable keeps track of the account balance, starting at zero. The function loops through each operation in the list, checking if the balance goes below zero. If so, it returns True. Otherwise, it returns False.