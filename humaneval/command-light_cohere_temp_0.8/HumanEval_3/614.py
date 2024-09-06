```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
```
Test it with the following operations:
```
# Examples
below_zero([1, 2, -4, 5]) # True
below_zero([1, 2, 3])        # False
```
This function uses a loop to iterate over each operation in the list. If the balance goes below zero, the function will immediately return True, indicating that the operation caused the account balance to fall below zero.

Additionally, the function will return False if the loop completes without reaching the condition or if the balance remains positive at the end.