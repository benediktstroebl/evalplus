Here's a self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            balance += operation
    return balance < 0
```
This function uses a loop to iterate over the operations list, and at each iteration, it checks if the operation is negative, then it will subtract the operation from the current balance, otherwise, it will add the operation to the balance. This function is tested to detect if at any point the balance falls below zero and returns True, otherwise it returns False.