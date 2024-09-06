```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
Do you have any other questions related to Python scripting, data structures, algorithms, or other programming concepts?