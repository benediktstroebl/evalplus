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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance goes negative at any point, the function returns `True`. Otherwise, it returns `False`. The function is tested against the provided test cases and is expected to pass. 
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
``` 
You can use this code to solve the problem and test it against other scenarios as well.