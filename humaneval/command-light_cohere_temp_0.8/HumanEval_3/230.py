Here's the updated Python script with self-contained function:
```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    """ >  
    
    # Initialize balance as 0
    balance = 0
    
    # Loop through operations
    for operation in operations:
        # If operation is -, then balance becomes - balance
        if operation == -1:
            balance *= -1
            
        # If balance becomes below zero, then return True
        elif balance < 0:
            return True
            
    # If balance is still positive, then return False
    return False
```
This script has a function `below_zero` that takes a list of operations as input and returns `True` if the balance of the account falls below zero at any point, and `False` otherwise.  The result:
1. The function first initializes the balance to 0.
2 It then loops through each operation in the operations list.
3. Inside the loop, the function checks if the current operation is `-`. If so, it will multiply the balance by -1, which effectively makes the balance become negative.
4. If the balance is less - then it will check if the balance is less than 0. If it is, the function will return `True`. Otherwise, it will return `False`.