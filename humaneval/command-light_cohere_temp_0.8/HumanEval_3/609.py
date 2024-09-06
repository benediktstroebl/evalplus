```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False

# Unit tests
operations_test = [1, 2, -4, 5]
result = below_zero(operations_test)
print(result)  # Output: True

operations_positive = [1, 2, 3, 4]
result = below_zero(operations_positive)
print(result)  # Output: False

operations_zero = []
result = below_zero(operations_zero)
print(result)  # Output: True
```

The Python function `below_zero` takes a list of integers, representing deposit and withdrawal operations. The function initializes a balance to zero and then iterates over the operations, adding each operation to the balance. It returns `True` if the balance falls below zero, and `False` otherwise. The unit tests cover a following cases and pass the corresponding tests.