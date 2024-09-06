Here is the corrected code for the provided markdown code block:
```python
def below_zero(operations):
    """You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    return False
```
The `below_zero` function takes a list of operations as input and returns a boolean value (`True` or `False`) depending on whether the balance of the account ever falls below zero during the operations. This function uses a strategy to iterate through each operation in the list, and checks the balance after each operation to see if it is less than zero. 

If the balance is already zero or goes below zero, the function will return `True`, indicating that the balance fell below zero during the operations.