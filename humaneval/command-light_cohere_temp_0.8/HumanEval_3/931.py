```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
# Test the function
[1, 2, -4, 5]


# Result: True
``` 
This function uses a loop to iterate over the list of operations and checks if the balance falls below zero at any point. If so, it returns True; otherwise, it returns False.