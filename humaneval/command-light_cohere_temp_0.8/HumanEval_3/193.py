Here is a self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```

This function takes a list of operations as input, where each element is either a deposit or a withdrawal from the account. It starts with an initial balance of 0 and iterates over each operation, adding the operation to the balance. The function returns True if at any point the balance becomes negative, indicating that the account balance has fallen below zero.