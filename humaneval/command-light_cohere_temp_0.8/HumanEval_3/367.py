```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Example usage:
# Operations: [-4, 5, 1, 2]
# Balance: -1
# Returns: True
below_zero([-4, 5, 1, 2])  #True
```
This Python script defines a function `below_zero` that checks if a list of operations on a bank account results in a balance below zero. The script uses a balance variable to keep track of the account balance and iterates over each operation in the list. When the balance becomes negative, the function returns `True` since the balance falls below zero. The script also uses a initial balance of 0, which is before any operations are applied.