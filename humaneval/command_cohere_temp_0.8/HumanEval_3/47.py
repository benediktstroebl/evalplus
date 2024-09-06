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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). The function simulates the progression of the account's balance after each operation and returns `True` if at any point the balance falls below zero, and `False` otherwise. 

Here is an example usage of the function:
```python
# Test the function with a list of operations
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
``` 

This test cases match the examples provided in the problem statement.