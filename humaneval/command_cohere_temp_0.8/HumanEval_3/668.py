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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance goes negative at any point, the function returns `True`. Otherwise, it returns `False`. The script passes the given tests of returning `False` for operations `[1, 2, 3]` and returning `True` for operations `[1, 2, -4, 5]`.  This way, the script fulfills the problem statement given in the markdown code block.