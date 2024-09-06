Here is a Python script that implements the function `below_zero` from the previous prompt, which solves the problem of checking for negative balance in a list of deposit and withdrawal operations for a bank account that starts from zero balance.

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Example usage
# [1, 2, -4, 5]  # list of operations
# True
```

This script defines a function `below_zero` that takes a list of operations as an argument. It iterates through loop through operations and maintains the balance, if at any point the balance falls below zero, it returns `True`. Otherwise, it returns `False`. 

This self-contained solution is a concise way to solve the problem and is a good example of how to create and use functions in Python.