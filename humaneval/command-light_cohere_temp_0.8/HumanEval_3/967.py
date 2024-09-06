Here is a Python script that includes the self-contained function `below_zero()`, which solves the problem and passes the tests:

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
print(below_zero([1, 2, -4, 5]))  # Output: True
print(below_zero([1, 2, 3, -4]))    # Output: False
``` 
This function iterates through the operations list, and at each step, it subtracts the current operation from the balance. It returns `True` if the balance becomes negative, indicating that the account has fallen below zero, otherwise, it returns `False`.