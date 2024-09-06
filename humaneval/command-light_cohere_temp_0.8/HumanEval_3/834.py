```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Example usage:
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
```
The function `below_zero` takes a list of operations as an argument and uses a loop to iterate over the operations. The function checks if the balance falls below zero after each operation and returns `True` if the balance is indeed negative. 

This function is self-contained and can be used to solve the problem of detecting a negative balance in a bank account. The function is designed to be efficient and can handle a large number of operations.

Note: The function assumes that all operations are deposits and will never go below zero. The function could be modified to handle withdrawals as well, by changing the loop to also check for withdrawals.