Here's the corrected Python script with the self-contained function below_zero that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise it should return False.
    
    >>> operations = [1,2,-4,5]
    """
    for operation in operations:
        if operation < 0:
            return True
    return False
``` 
The function checks each element in the list operations to see if it's less than zero. If any element is less than zero, the function will immediately return True, as this is the condition to check for.