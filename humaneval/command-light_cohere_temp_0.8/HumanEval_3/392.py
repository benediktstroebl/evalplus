Here is a self-contained Python script that solves the problem of checking if the balance of a bank account ever falls below zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance -= operation
    return balance < 0
```
This function takes a list of operations as an argument, where each operation is a withdrawal from the account. It initializes a balance to 0, then iterates through each operation in the list, subtracting the operation from the balance. This process continues until the balance falls below 0, at which point the function returns True, indicating that the balance has fallen below zero at least. Otherwise, it returns False.