Here is a Python script that includes a self-contained function, `below_zero()`, that solves the problem you provided:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
The `below_zero` function takes a list of integers, `operations` as an argument. It initializes the fuc balance with 0, then loops through the `operations` list, adding each operation to the balance. At the end of the the loop, it returns `True` if the balance falls below 0, and `False` otherwise. 

This self-contained function demonstrates the logic required to solve the problem, and passes the test you provided.