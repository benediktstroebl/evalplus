Here's the Python script that provides a self-contained function `below_zero` to solve the problem you've described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
        if balance < 0:
            return True
    return False
# Test cases
>>> below_zero([1, 2, -4, 5])
True
>>> below_zero([1, 2, 3, -4])
False
>>> below_zero([-1, 2, -3, 4])
True
>>> below_zero([100, 50, 0, -40])
False
>>> below_zero([-1, -100, -3, -4])
True
```

The function iterates through each element in the list of operations and accumulates the effect of each operation on the balance variable. The function then checks if the balance is less than zero and returns `True` if true. Otherwise, it returns `False`.