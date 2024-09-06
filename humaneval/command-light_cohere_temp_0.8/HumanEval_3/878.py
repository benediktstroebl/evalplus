Here is a self-contained Python function that solves the problem you described: 

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

This function takes a list of operations as input, where each operation is an integer that represents a deposit or withdrawal from the bank account. The function initializes a balance of the account to 0 and then iterates through the operations, checking if the balance ever falls below zero. If the balance ever falls below zero, the function returns True. Otherwise, it returns False.

This function is self-contained and does not rely on any other functions or modules, which means it can be easily tested and used in other contexts. 

You can call this function and pass your test cases to see if it works correctly.