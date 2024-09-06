```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This function below_zero takes a list of operations as input and uses a balance variable to iterate through each operation, ultimately returning True if the balance falls below zero and False otherwise.