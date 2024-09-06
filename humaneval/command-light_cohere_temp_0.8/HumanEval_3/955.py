Here's the code:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False
```
This code defines a function called `below_zero` that takes a list of integers as an argument. It then initializes a balance to 0, and then loops through the list of operations. If any operation is positive, it adds the operation to the balance, and if any operation is negative, it returns True, indicating that the balance has gone below zero.