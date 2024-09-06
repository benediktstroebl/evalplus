```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False

# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True

operations = [1, 2, -3, -5]
result = below_zero(operations)
print(result)  # Output: False
```
This script defines a function called below_zero that takes a list of integers as input. It initializes a initial balance to zero and then iterates over the operations, checking if the balance ever falls below zero. If the balance ever falls below zero, the function returns True; otherwise, it returns False. 

The example usage demonstrates how to call the function with a list of operations and prints the result.