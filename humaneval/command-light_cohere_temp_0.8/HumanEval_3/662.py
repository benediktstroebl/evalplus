```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Examples
below_zero([1, 2, -4, 5])  # True
below_zero([1, 2, -3, -1])  # False
```
This code defines a function below_zero that takes a list of operations as input and returns a boolean value indicating whether the balance falls below zero at any point in the list. It achieves this by initializing the balance to 0 and then iteratively deducting each operation from it. If the balance becomes negative at any point, the function will return True, otherwise it will return False.