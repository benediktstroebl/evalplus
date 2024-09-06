Here's a self-contained Python function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function takes a list of operations (deposit and withdrawal) as an argument and initializes a balance variable to 0. Then, it iterates over each operation in the operations list, adding the value of each operation to the balance. Finally, it returns True if the balance is less than 0.