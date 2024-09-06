```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    >>> operations = [1, 2, -4, 5]
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This function takes a list of operations and uses a loop to iterate through each element. It then uses a balance variable to keep track of the account balance, starting with an initial balance of 0. It then adds each operation in the list to the balance and checks whether the balance is less than 0.