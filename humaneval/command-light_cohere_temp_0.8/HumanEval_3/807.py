```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function uses a loop to iterate over the operations in the input list. It initializes a balance with 0, then adds each operation from the list to the balance. The function returns True if the balance falls below 0 at any point in the loop, otherwise it returns False.