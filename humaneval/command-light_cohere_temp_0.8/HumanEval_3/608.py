Here is a self-contained Python function that solves the problem you described:

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
The function `below_zero` takes a list of operations as input and uses a loop to iterate over each operation. 

It then subtracts each operation from the balance, and if the balance falls below zero, it returns `True`. Otherwise, it returns `False`. 

You can test the function using the provided test cases and verify that it works as expected.