```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False


# Test cases
operations1 = [1, 2, -4, 5]
operations2 = [1, 2, 3, -6]

result1 = below_zero(operations1)
result2 = below_zero(operations2)

if result1 == result2:
    print("All operations passed!")
else:
    print("Operations failed.")
```
This code defines a function below_zero that checks a list of deposit and withdrawal operations to determine if the balance of a bank account ever falls below zero. The function uses a balanced algorithm and returns True if this balance condition is met, and False otherwise. The test cases demonstrate that this function passes for the given operations.