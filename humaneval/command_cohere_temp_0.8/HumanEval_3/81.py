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

The script defines a function `below_zero` that takes a list of `operations` as input, representing deposit and withdrawal operations on a bank account. It initializes the balance to 0 and iterates through each operation in the list. It updates the balance accordingly and checks if it falls below 0 at any point. If the balance ever goes negative, it immediately returns `True`, otherwise, it returns `False` at the end of the loop when all operations are processed.

Here is an example usage:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```