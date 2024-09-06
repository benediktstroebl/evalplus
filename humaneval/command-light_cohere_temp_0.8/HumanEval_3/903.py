```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            return True
    return balance < 0
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
```

This code defines a function `below_zero` that takes a list of integers as input and returns a boolean value that indicates if the balance of the account falls below zero. The balance is initially set to zero, and the loop goes through each operation in the list. If the operation is positive, the balance is increased, and if it is negative, the function immediately returns `True`. The test code provided is an example of how to use the `below_zero` function with a list of operations and prints the result.