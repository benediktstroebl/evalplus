Here is a self-contained Python script that solves the problem you provided: 
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance -= operation
    return balance < 0
```
The `below_zero` function takes a list of operations as input and initializes the balance variable to 0. Then, it iterates through operations and continuously subtracts the operation from the balance until the balance falls below zero, at which point the function returns `True`. 
To test the function, you can pass a list of operations and it should return `True` if the balance is below zero, otherwise it should return `False`.