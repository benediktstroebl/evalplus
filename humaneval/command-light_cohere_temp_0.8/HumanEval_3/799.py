```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
The function below_zero takes a list of operations as an input. It initializes the a balance to 0. It then iterates over each operation and if the balance goes below 0, it returns True. If the loop completes without any operations causing the balance to go below 0, it means the balance is already at 0 and there are no operations to add, so the function returns False.