```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. The function calculates the net balance of the bank account by iterating through the list of operations, summing up the deposits and withdrawals. Then, it checks if the net balance falls below zero at any point. If the balance is ever negative, it immediately returns `True`, indicating that the account balance fell below zero at least once. If no negative balance is encountered, it returns `False` at the end of the operations list.

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This output is consistent with the original markdown description.