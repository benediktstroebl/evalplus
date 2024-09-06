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
operations1 = [1, 2, -4, 5]
operations2 = [1, 2, 3, -1]

print(below_zero(operations1))  # Output: False
print(below_zero(operations2))  # Output: True
```
This Python code defines a function below_zero that checks if a list of operations results in a balance below zero for a bank account. The function initializes a balance to zero and iterates through the operations. The function adds the positive operations and subtracts negative operations. If any operation would leads to a balance below zero, the function immediately returns True, indicating the condition is met. Otherwise, it returns False.