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

This script defines a function `below_zero` that takes in a list of `operations` (of type `List[int]`), which represent the sequence of deposit and withdrawal operations on a bank account. The function initializes the balance to 0 and then iterates through each operation in the list. It updates the balance by adding or subtracting the value of each operation. If at any point the balance falls below 0 (indicating a negative balance), it immediately returns `True`. If no such negative balance is encountered, it returns `False` at the end of the loop, indicating that the account never fell below zero during the given operations. 

This solution follows the given test examples provided in the markdown code block and will return accordingly:
- `False` for the first test example `[1, 2, 3]` since the account balance never falls below zero.
- `True` for the second test example `[1, 2, -4, 5]` due to the account balance falling below zero after the `-4` withdrawal operation, and the function will return `True`.