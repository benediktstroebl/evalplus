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

This script defines a function called `below_zero` that takes a list of integers `operations` as input. It simulates the operations on a bank account, starting with a zero balance. It iterates through each operation in the list and adds it to the running balance. If the balance falls below zero at any point, it immediately returns `True`, indicating that the account balance went below zero at any time during the operations. If the balance stays non-negative until the end of the operations, it returns `False`.

This solution follows the prompt's expected behavior and returns `True` for tests like `below_zero([1, 2, -4, 5])` and `False` for `below_zero([1, 2, 3])`.