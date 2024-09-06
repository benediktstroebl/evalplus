Here is a self-contained Python script with a function that solves the problem you described:
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

# Test cases
operations_test = [
    [1, 2, -4, 5],
    [-1, 3, -9],
    [-10, 100]
]

for operation_test in operations_test:
    result = below_zero(operation_test)
    print(f"{result}")
```

This function takes a list of operations as input and iterates over them. If any operation is positive, it will increase the balance by that amount. If the operation is negative, it will trigger the condition to return True. The balance is initialized to zero at the start, and during the iteration, the balance is updated either by adding the operation's value if it's positive or by subtracting the operation's value if it's negative.