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
result = below_zero(operations)
print(result)  # Output should be True
``` 
This code is a Python script with a self-contained function below_zero that solves the problem and passes the tests.