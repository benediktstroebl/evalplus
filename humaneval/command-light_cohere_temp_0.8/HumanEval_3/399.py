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
This function takes a list of operations as an argument, where each operation can be either a deposit or a withdrawal from the account. The function then initializes a balance to 0, and iterates through each operation in the list. If at any point the time, the balance becomes negative, it will return True, indicating that the balance of the account has fallen below zero. Otherwise, the function will return False, indicating that the balance of the account has not fallen below zero.