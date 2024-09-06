```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False

# Test the function
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
```
The function below_zero takes a list of operations as input and iterates through each operation in the list. It checks if the balance falls below zero. If it does, the function returns True, indicating that the balance has fallen below zero. If the balance remains non-negative throughout all operations, the function returns False.