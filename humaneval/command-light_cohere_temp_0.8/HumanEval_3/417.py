```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
``` 
This code defines a function `below_zero` that takes a list of integers as its parameter `operations`. It performs a loop over all the operations in the list, where the balance is initialized to 0. The code then checks if the balance is less than 0 at the end of each operation and returns True if it's the case, otherwise it returns False.