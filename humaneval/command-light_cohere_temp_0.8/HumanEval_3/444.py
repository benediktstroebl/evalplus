Here's the code:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function takes a list of operations as input and uses a loop to iterate through each operation. The balance is then increased by each operation. If at any point the local balance falls below zero, the function returns True, indicating that the account balance has fallen below zero. If the balance is greater than or equal to zero at the end of the loop, the function returns False, indicating that the balance was not below zero.

This is a self-contained Python script that solves the problem of checking if the balance of a bank account falls below zero, using a simple loop and conditional check.