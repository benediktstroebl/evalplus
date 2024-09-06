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
This code defines a function called `below_zero` that takes a list of integers `operations` as an argument. It initializes a generate a variable `balance` and sets it to 0. Then, it iterates through the operations and for each operation that would cause the balance to go below 0, it returns True. If none of the operations would affect the balance to go below 0, it returns False after the loop completes.