Here's the self-contained Python script with a function `below_zero` that solves the problem:

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

The function uses a loop to iterate over each operation in the list. Each operation is added to the balance variable, which starts at zero. If at any point the balance goes below zero, the function will return `True`. Otherwise, it will return `False`.

This function is fully self-contained and does not require any external modules or functions. It can easily be used to solve the problem of detecting if the balance of a bank account falls below zero.