```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function checks if the balance falls below zero after adding all operations. The function is self-contained, it does not require any external functions or modules.