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

The `below_zero` function iterates through the list of `operations`, summing them to the `balance`. If the `balance` is less than 0 at any point, it returns `True`. Otherwise, it returns `False` at the end of the iteration if the balance remained positive.  This solution follows the instructions and passes the tests provided in the spec.