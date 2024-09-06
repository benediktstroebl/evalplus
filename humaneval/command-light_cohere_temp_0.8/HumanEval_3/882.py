Here's the self-contained Python script with the function `below_zero` that solves the problem:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```

This function takes a list of operations (deposit and withdrawal) and uses a loop to iterate through each operation. The function starts with an initial balance of 0 and then adds each operation to the balance. The function then checks if the balance is less than 0 and returns `True` if true. If the balance doesn't fall below zero, the function returns `False`.