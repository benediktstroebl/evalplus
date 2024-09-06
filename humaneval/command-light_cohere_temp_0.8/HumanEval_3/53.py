Here's a Python script with a self-contained function that solves the problem you've described: 

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    # Your function here!
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
```

This function takes a list of operations as an argument and uses a loop to iterate through the operations. The function adds each operation to the current balance, and if the balance falls below zero, it returns `True`. If the balance doesn't fall below zero, the function returns `False`.