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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). It calculates the balance by summing up the operations, then checks if it goes negative at any point, and returns `True` if it does, and `False` otherwise. The function is tested with example operations where it returns true for a negative balance and false in the example where the balance is positive throughout. 
Here is an example of how to use the function:
```python
>>> below_zero([1, 2, -4, 5])
True
>>> below_zero([1, 2, 3])
False
``` 
This will return True for the first case because the balance will be negative after the third operation of `-4` and will return false for the second case as the balance never falls below zero.