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
This function iterates through a list of operations, where each operation is either a deposit or a withdrawal from the account balance. The function starts with an balance of 0 and updates it by the operations. The function checks if the balance becomes negative at any point, and if it is, the function returns True, indicating that the balance fell below zero. If the balance remains positive after processing all operations, the function returns False, indicating that the balance did not fall below zero.