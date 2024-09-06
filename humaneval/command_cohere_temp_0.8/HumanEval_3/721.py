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

This script defines a function called `below_zero` that takes a list of integers `operations` as input. It simulates the operations done on a bank account, starting with a zero balance. It iterates through each operation in the list and adds it to the running balance. If the balance falls below zero at any point, it immediately returns `True`, indicating that the account balance fell below zero at any point during the operations. If the balance stays non-negative until the end of the operations, it returns `False`. 

Here is an example usage:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```
This passes the provided tests, correctly identifying that the balance falls below zero with the second example operations list.