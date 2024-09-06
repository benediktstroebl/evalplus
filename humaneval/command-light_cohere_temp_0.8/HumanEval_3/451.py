```Python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
``` 
The function below_zero takes a list of operations as an argument and returns a boolean value that is True if the balance falls below zero, and False otherwise. It iterates through operations and adds them to the balance.