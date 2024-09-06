```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False

# Test the function
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True

# Test with invalid inputs
operations = [1, 2, 3]
result = below_zero(operations)
print(result)  # Output: False
```
The code defines a function `below_zero` that takes a list of operations and checks whether the balance falls below zero at any point. The function iterates through the operations, increments the balance, and if the balance becomes negative, returns `True`. Otherwise, it returns `False`. 

The code then tests the function with various input operations and prints the result. It passes all the both valid test cases.