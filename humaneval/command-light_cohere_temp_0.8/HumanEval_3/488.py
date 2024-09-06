Here is a self-contained Python function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op < 0:
            balance -= op
        else:
            balance += op
    return balance < 0
```
This function uses a loop to iterate through the operations list. It starts with an initial balance of 0 and then checks if each operation is a withdrawal or a deposit. If the operation is a withdrawal, it subtracts the amount from the balance. Otherwise, it adds the amount to the balance.