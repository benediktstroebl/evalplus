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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the ending balance is less than zero, the function returns `True`, otherwise, it returns `False`. 

Here is an example usage of the script:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

The first example states that with operations `[1, 2, 3]`, the ending balance will be `2` which is not less than zero, therefore, the function returns `False`. The second example shows that with operations `[1, 2, -4, 5]`, the ending balance will be `-2` which is less than zero, so the function returns `True`.