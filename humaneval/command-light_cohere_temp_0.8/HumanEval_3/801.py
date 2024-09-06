Here is the code:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
This code defines a function below_zero that takes a list of operations as an argument. The function performs the detection of operations that cause the balance of the account to go below zero. The function uses a balanced start at 0, and iterates through each operation in the list. If the balance falls below zero, the function returns True; otherwise, it returns False.