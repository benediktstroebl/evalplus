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

This script defines a function called `below_zero` that takes in a list of integers called `operations`. This function calculates the balance of the bank account by adding up all the operations and checks if the balance ever falls below zero, and returns a boolean indicating whether the balance went negative at any point.

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

This would return False for the first example, since the balance never falls below zero. For the second example, the balance first rises to 3, then falls to -2, and then rises to 5, so it returns True.