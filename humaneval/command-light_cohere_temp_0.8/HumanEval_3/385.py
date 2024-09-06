```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Example usage
below_zero([1, 2, -4, 5]) # returns True
```
This function takes a list of operations, then it starts with an initial balance of 0 and iterates through the list of operations. If at any point the unmistakable, the balance goes below zero, the function will return True. Otherwise, it returns False.