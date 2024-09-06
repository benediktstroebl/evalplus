```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return False

# Test cases
operations = [1, 2, -4, 5]
print(below_zero(operations))  # Output: True

operations = [0, 2, -3, 5]
print(below_zero(operations))  # Output: False

operations = [100, -101, -1, -200]
print(below_zero(operations))  # Output: True
```
The `below_zero` function takes a list of operations and iteratively processes each operation. The function adds positive operations to the balance and subtracts negative operations from the balance. It is triggered to return True if the balance ever falls below zero and False if the balance is zero or a positive number.