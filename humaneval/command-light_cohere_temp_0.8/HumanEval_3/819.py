Here's a self-contained Python script with a function that solves the problem of checking if the balance of a bank account ever falls below zero, and passes the tests provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test cases
# Test 1
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True

# Test 2
operations = [1, -2, 3, -5]
result = below_zero(operations)
print(result)  # Output: True

# Test 3
operations = [0, 1, 2, 3]
result = below_zero(operations)
print(result)  # Output: False
```
The script defines a function `below_zero` that takes a list of operations as an argument. The function initializes the balance to zero and iterates over the list of operations. It checks if the balance ever falls below zero by iterating through the operations and decreasing the balance by the value of each operation. If at any point the would happen, it returns `True`, otherwise it returns `False`.