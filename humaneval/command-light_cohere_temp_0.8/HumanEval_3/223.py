Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
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
This function takes a list of operations as input and initializes a balance variable to 0. The function then loops through each operation in the list, adding the operation to the balance. If the balance falls below 0, the function returns True, indicating that the balance is below zero. Otherwise, it returns False.