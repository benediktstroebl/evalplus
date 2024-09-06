```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
```
This script defines a function called below_zero, which takes a list of operations as an argument. The function loops through each operation in the list, and if it makes the balance of the account go below zero, it returns True. Otherwise, it returns False.

This solution is self-contained and uses the balance variable to keep track of the account balance.