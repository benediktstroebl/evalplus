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

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. It initializes the balance to 0 and then iterates through each value in the input list. It adds each operation to the current balance and checks if it falls below 0. If the balance is less than 0 at any point, it immediately returns `True`. Otherwise, it returns `False` after processing all operations if the balance never fell below zero.

Here is an example usage of this function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This output is consistent with the provided example in the problem statement. The first case should return `False` since the balance is always greater than zero. The second case should return `True` because the balance becomes negative after the second operation.