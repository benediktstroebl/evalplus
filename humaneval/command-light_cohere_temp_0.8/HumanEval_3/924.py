```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function takes a list of operations as input and uses a loop to iterate over each operation, adding the operation to the balance. This ensures the balance stays positive and thus we are able to detect operations that cause the balance to go below zero.