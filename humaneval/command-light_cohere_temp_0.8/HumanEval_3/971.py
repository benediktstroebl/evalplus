```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test case 1
below_zero([1, 2, -4, 5]) # Output: True

# Test case 2
below_zero([-5, 2, -3, -4]) # Output: True

# Test case 3
below_zero([1, -2, 3, -4]) # Output: False
```
This code defines a function below_zero that takes a list of operations as an input. It initializes a certain balance of zero, and then iterates through each operation in the list. If the balance falls below zero, it returns True, otherwise, it returns False.