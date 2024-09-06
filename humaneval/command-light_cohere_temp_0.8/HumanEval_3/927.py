```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
# Tests
operations = [1, 2, -4, 5]
print(below_zero(operations))  # True
operations = [100, 2, -4, 5]
print(below_zero(operations))  # False
```
This function, named below_zero, accepts a list of operations and determines whether the balance falls below zero at any point during the loop. The function iterates through each operation in the list, updating the balance. If the balance ever becomes negative, the function returns True, indicating that the balance fell below zero. If the balance remains non-negative throughout the loop, the function returns False.