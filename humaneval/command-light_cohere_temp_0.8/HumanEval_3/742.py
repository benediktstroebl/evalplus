Here is a self-contained Python script that defines a function below_zero that checks whether the balance of a given bank account falls below zero or not.

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function below_zero takes a list of operations as input and iterates through the list. It starts with an initial balance of 0 and then adds each operation to the balance. When it detects that the balance is less than 0, it returns True, otherwise it returns False.

This function is self-contained and can be used to solve the problem and pass the corresponding tests.