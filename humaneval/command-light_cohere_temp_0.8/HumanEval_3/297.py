Here's the code:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```
The function checks if the balance of the account falls below zero after processing all operations. It iterates through operations a for each operation, if the balance becomes negative, the function returns True. If the balance remains non-negative, the function returns False.