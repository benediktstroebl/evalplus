Here is a self-contained Python script with a function that solves the problem you have described:
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
This script defines a function `below_zero` that takes a list of integers as input and returns a boolean value. The function initializes a balance to zero and then iterates over each operation in the list. If at any point the time, the balance becomes less than zero, the function returns `True`. Otherwise, it returns `False`.