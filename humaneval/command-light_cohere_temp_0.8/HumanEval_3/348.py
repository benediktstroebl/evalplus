Here's the self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
The function uses a loop to iterate over the list of operations, subtracting each operation from the balance. Then, it checks if the balance is less than 0, which indicates that the balance has fallen below zero. If this is the is the case, the function returns True. Otherwise, it returns False, indicating that the balance is still non-negative after processing all the operations.