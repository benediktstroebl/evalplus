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

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. It initializes the balance to 0 and then iterates through each value in the input list. It adds each operation to the running balance, and if the balance ever goes negative, it immediately returns `True`. If no negative balance is encountered, it returns `False` at the end of the operations list.

Here is an example usage of this function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```
This corresponds to the example usage provided in the problem statement.