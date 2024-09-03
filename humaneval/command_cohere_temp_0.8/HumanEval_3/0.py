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

This script defines a function called `below_zero` that takes in a list of integers `operations` as input. It initializes the balance to 0 and iterates through each value in the input list. It assumes that each integer represents an operation on a bank account where a positive integer represents a deposit, and a negative integer represents a withdrawal. It keeps a running balance of these operations and returns `True` if the balance ever falls below zero, and `False` otherwise. It returns `False` if there are no negative numbers in the input list. 

Here is an example:
```python
assert below_zero([1, 2, 3]) == False
assert below_zero([1, 2, -4, 5]) == True
``` 
This passes the provided test examples.