```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

The `below_zero` function iterates through the list of operations, accumulating the balance while keeping track of the running total. If at any point the balance falls below zero, it immediately returns `True`. Otherwise, it returns `False` at the end if the balance remained non-negative. 

This approach takes advantage of the linear time complexity of Python's list comprehension and basic arithmetic operations for a straightforward problem-solving approach.