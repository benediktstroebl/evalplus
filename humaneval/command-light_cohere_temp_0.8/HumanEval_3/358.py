Here is a Python script that includes a self-contained function that solves the problem of detecting if the balance of a bank account ever falls below zero:
```python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        elif balance < 0:
            return True
    return False
```
This function takes a list of operations, where each operation could be a deposit or a withdrawal, as input and uses a simple loop to iterate through each operation. It maintains a balance at 0 and if any operation would decrease the balance below 0, it returns True. Otherwise, it returns False.

This code is self-contained, and you can use it to solve the problem of detecting if the balance of a bank account ever falls below zero.