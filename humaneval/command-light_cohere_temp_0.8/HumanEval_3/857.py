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
# Example usage:
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
``` 
This Python code defines a function called below_zero that takes a list of operations as an argument. The function iterates through the operations, keeping track of the balance in a variable called balance. It initializes the example usage to test the function with a list of operations [1, 2, -4, 5]. The expected output is True, indicating that the function correctly detects that the balance of the account falls below zero.