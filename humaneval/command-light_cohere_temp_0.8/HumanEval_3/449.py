```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
```
This Python code defines a function called below_zero that takes a list of integers as input. It iterates over each operations and checks if the balance of the account ever falls below zero. If it does, it returns True, indicating that the account balance went below zero. Otherwise, it returns False. 

The code then demonstrates the usage of the function with an example list of operations.