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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the balance of the bank account after each operation. If at any point the balance falls below zero, the function returns `True` indicating that the balance went below zero at least once. Otherwise, it returns `False`.

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This function is self-contained and can be safely copied and pasted into a Python environment to test and use as required.  If you have any more questions or need further assistance, feel free to ask!