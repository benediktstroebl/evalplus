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

This script defines a function `below_zero` that takes in a list of `List[int]` and calculates the ending balance after each operation. If the balance ever falls below 0, the function returns `True`. Otherwise, it returns `False`.

Here is an example usage of the script:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
```

The first example outputs `False` because the list of operations `[1, 2, 3]` result in a final balance of `2` which is greater than 0. The second example outputs `True` because the list of operations `[1, 2, -4, 5]` result in a final balance of `-2` which is less than 0.