```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks whether the operations result in a balance below zero at any point.
    :param operations: List of operations where each element is either deposit or withdrawal
    :return: True if operations result in balance < 0 at any point, False otherwise
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        if op > 0:  # deposit
            balance += op
        elif op < 0:  # withdrawal
            balance -= op
    return False
```