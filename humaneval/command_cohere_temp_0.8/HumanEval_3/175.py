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

This Python script defines a function called `below_zero` that takes a list of integer operations and tests if any point the balance of operations result in a value less than 0. The function updates the balance variable by adding the value of the operation to it. If the balance ever goes negative, the function returns True. Otherwise, it returns False. 

Here is an example usage of this function:
```python
>>> below_zero([1, 2, 3])
False
>>> below_zero([1, 2, -4, 5])
True
``` 
This would return False and True for the respective operations given as it does not go below zero and goes below zero respectively.