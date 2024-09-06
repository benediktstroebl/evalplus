```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
#Test case
below_zero([1, 2, -4, 5]) #True
```
This function takes a list of operations and iterates through each operation in the list. It subtracts each operation from the balance and checks if the balance becomes negative. If it does, it returns True, indicating that the account balance has fallen below zero. If the loop completes without the balance becoming negative, the function returns False, indicating that the balance was not below zero.