```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, -4, 5, 6])
    False
    >>> below_zero([10, -4, 5])
    False
    >>> below_zero([])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```