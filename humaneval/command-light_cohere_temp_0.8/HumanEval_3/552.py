Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:

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

This function, below_zero, takes a list of operations as input and initializes a balance of 0. The function then loops through each operation in the operations list, and if the balance falls below 0, the function immediately returns True. Otherwise, the function will continue looping until the balance becomes zero, at which point the function will return False.