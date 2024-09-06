Here is a self-contained Python script that solves the problem you described:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False

# Example usage
# Pass the operations list to the function
operations = [1, 2, -4, 5]
result = below_zero(operations)

if result:
    print("Below zero balance!")
else:
    print("Not below zero balance.")
```

This script defines a function `below_zero` that takes a list of operations as an argument. It initializes thea balance to zero, and then iterates through the operations, checking if the balance falls below zero. If it does, it returns `True`. Otherwise, it returns `False`. The example usage demonstrates how to call the function with a list of operations and print the appropriate output.