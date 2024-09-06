Here's a self-contained Python script that solves the problem you provided: 
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
 >>> below_zero([1, 2, -4, 5])
 True
>>>below_zero([1, 2, 3, -1])
 False
>>>below_zero([10, -10])
 False
>>>below_zero([-10, -20])
 True
``` 
This script defines a function `below_zero` that checks whether the balance of the account falls below zero. It uses a `List` as the input, which is a list of operations, and iterates through each operation in the list. If the balance falls below zero, the function returns `True`. Otherwise, it returns `False`.