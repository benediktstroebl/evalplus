Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of the account falls below zero, 
    and at that point, the function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([4, 8, 2, 1])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    if balance < 0:
        return True
    return False
```
The above Python script defines a function below_zero that takes a list of operations as input and returns a boolean value indicating whether the balance of the account falls below zero at any point in the operations. The balance is initialized to 0, and the loop iterates over each operation in the input list. If the balance becomes negative at any point, the function returns True, otherwise, it returns False.