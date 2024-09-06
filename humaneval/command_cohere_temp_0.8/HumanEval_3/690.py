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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance goes negative at any point, the function returns `True`, otherwise, it returns `False`. The function is encapsulated and doesn't rely on any external variables to work, making it self-contained. 

To test this function, you can use the following inputs:
- `[[1, 2, 3]]` -- Should return `False`
- `[[1, 2, -4, 5]]` -- Should return `True`

Both of these tests represent different operations on a bank account that starts with a balance of 0. The first one does not cause the account to go below zero, whereas the second one does.