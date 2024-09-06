Here's the provided Python script:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        elif balance < 0:
            return True
    return False

# Example usage
# Operations given as a list of integers
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
```
This function below_zero takes a list of operations and checks whether the balance of the account falls below zero at any point. If the balance ever goes below zero, the function will return True, otherwise, it will return False.