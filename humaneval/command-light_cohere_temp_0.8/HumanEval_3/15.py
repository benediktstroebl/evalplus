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
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
``` 
This code defines a function `below_zero` that takes a list of operations and checks whether the balance of the account ever falls below zero.  The script then demonstrates the function using a sample list of operations and prints the result.