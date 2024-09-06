```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. The function initializes a variable `balance` to zero, and then iterates through each value in the input list. It adds each operation to the running total `balance`, and checks if it goes negative at any point. If it does, the function returns `True`, and if it completes all operations without going negative, it returns `False`. 

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```
This will return `False` for the first case because the balance is never negative, and `True` in the second case because it goes negative with the `-4` operation.  This matches the test cases specified in the problem.