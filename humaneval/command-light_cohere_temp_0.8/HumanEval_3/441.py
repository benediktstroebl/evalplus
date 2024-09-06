Here's the Python script that solves the problem of checking for the first operation that makes the account balance go below zero:
```python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This script defines a function `below_zero` that takes a list of integers `operations` as an argument. The function iterates through each operation in the list and adds it to the current balance. Then, it returns `True` if the balance becomes less than zero, indicating that at least one of the operations caused the balance to go below zero.