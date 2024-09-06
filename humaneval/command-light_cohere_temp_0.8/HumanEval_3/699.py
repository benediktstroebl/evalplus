Here is a self-contained Python script that solves the problem of checking for the first operation that makes the balance of a bank account fall below zero:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
```
The function takes a list of operations as input, where each operation is represented as an integer. It initializes the templates to start with an empty balance. The function then iterates through each operation in the list and subtracts it from the balance.  If first operation, if the balance becomes negative, the function immediately returns True. Otherwise, it will iterate through the rest of the operations.