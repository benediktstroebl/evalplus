Here is a self-contained Python script with a function that solves the problem and passes the corresponding tests:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance += operation
    return False

# Test cases
operations = [1, 2, -4, 5]
test_below_zero = below_zero(operations)
print("Test 1:", test_below_zero)

operations = [0, 2, -4, 5]
test_below_zero = below_zero(operations)
print("Test 2:", test_below_zero)

operations = [1, -5, 3, -3, 4]
test_below_zero = below_zero(operations)
print("Test 3:", test_below_zero)
```
The provided code defines a function called below_zero, which takes a list of operations as input. It starts with an initial balance of 0 and iterates through the operations, checking if the balance falls below zero. If it does, the function returns True. Otherwise, it returns False. The code also provides three test cases, where the function is called with different operations lists.