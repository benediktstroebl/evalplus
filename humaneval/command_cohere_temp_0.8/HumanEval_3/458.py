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

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. The function iterates through each value in the input list and accumulates the balance of the bank account. If at any point the balance falls below zero, it indicates a negative balance and the function returns `True`. If the balance remains non-negative throughout, it returns `False`.

Here's an example usage demonstration that reproduces the test cases from the original problem:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
``` 
This demonstrates the function's behavior, correctly identifying `False` for the first example and `True` for the second.