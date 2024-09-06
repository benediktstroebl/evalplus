```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This script defines a function called below_zero, which takes a list of operations as an argument. It initializes a balance with 0, and then iterates through the operations, adding their values to the balance. The function returns True if the balance falls below 0, and False otherwise.