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

This script defines a function `below_zero` that takes a list of `operations` as input, where each element represents an operation on a bank account (either a deposit or withdrawal). The function iterates through each operation in the list, updating the running balance by adding the `op`. If at any point the balance falls below zero, it immediately returns `True`, indicating that the account balance went negative at some point. If none of the operations cause the balance to go negative, it returns `False` at the end. 

This solution is concise and efficiently solves the problem by maintaining a single variable, `balance`, to keep track of the current account balance as each operation is applied. 

The `below_zero` function can be tested directly within the Python interpreter by calling it with different operation lists and verifying the returned results against the expected truth values. 

For example:
```python
# Test case 1
print(below_zero([1, 2, 3]))  # Expected output: False

# Test case 2
print(below_zero([1, 2, -4, 5]))  # Expected output: True
``` 
```