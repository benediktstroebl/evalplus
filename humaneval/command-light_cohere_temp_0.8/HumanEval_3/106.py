Here is the self-contained Python function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            break
    return balance < 0
```
This function takes a list of operations as input and iterates through each operation in the list. It checks if the results in the list are negative, then it subtracts the result from the balance. If any operation is non-negative, it breaks out of the loop. Finally, it returns True if the balance is less than zero, indicating a balance below zero.