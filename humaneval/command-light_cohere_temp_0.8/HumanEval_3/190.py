Here's the self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```
This function takes a list of deposit and withdrawal operations as an argument and iterates through each operation. It maintains a record of the balance and updates the balance after each operation. If at any point the example operations have a negative value, the balance will go below zero and the function will return True. If the balance remains non-negative after all operations, the function will return False.

This function is self-contained and can be used to solve the problem and pass the test with the provided markdown code block.