```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
The function checks the given operations against a balance variable and returns True if the balance ever falls below zero. The test cases are also provided to show the functionality. The function follows the simple logic of keeping track of balance and detecting the first operation that makes the balance go negative.