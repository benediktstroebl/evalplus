```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    >>> operations=[1, 2, -4, 5]
    ```
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
This function uses a loop to iterate through a list of deposit and withdrawal operations and keeps track of the account balance. It adds each operation to the balance and checks whether the balance is below zero, returning True if it is and False otherwise.