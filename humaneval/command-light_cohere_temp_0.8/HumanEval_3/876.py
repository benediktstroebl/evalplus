Here's the solution using Python:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0: balance += operation
        elif operation < 0: balance -= operation
    return balance < 0
```
The function uses a loop to iterate through the list of operations. It adds positive operations to the balance if the operation is positive and subtracts the operation if it's negative. 
This function is self-contained and uses the balance variable to keep track of the account balance.