```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
The function takes a list of operations as an argument, and iterates through the list. The function tracks the balance of the account, and at each step, it subtracts the value of each operation from the balance. When the balance reaches a negative value, the function returns `True`, indicating that the balance is below zero. The function would also return `False` if the balance is non-negative throughout the loop.