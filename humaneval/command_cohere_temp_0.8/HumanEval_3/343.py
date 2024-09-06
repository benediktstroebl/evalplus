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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ongoing balance of the bank account after each operation. If at any point the balance goes below zero, the function returns `True`. Otherwise, it returns `False`. 

Here is an example usage of the function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
``` 
This would return `False` for the first case because the balance never goes below zero. In the second example, the balance goes negative after the third operation, so the function returns `True`. 

This accurately solves the problem and passes the tests given in the prompt.