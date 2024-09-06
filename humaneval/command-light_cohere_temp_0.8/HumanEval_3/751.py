```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Checks if at any point, the balance of the account goes below zero
    """
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False
# Test the function
if below_zero([1, 2, -4, 5]):
    print("The balance went below zero.")
else:
    print("The balance was not below zero.")
``` 
The code defines a function below_zero that checks whether the balance of the account goes below zero after processing the given operations. It initializes the another loop iterates each element in the operations list and adds it to the balance, if the balance goes below zero, it will return True, otherwise it will return False.