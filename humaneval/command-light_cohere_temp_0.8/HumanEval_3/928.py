Here is a Python script with a self-contained function that solves the problem and passes the tests provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
```
This function takes a list of operations as an argument and uses a loop to add each operation to the balance. It then checks if the balance is less than 0, and if so, it returns True, indicating that the account balance fell below zero. If the balance is not negative, it returns False.