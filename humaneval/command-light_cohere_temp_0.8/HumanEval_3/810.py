Here's a self-contained Python function that solves the problem you described:
```python
def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([10, -2, -20, -15])
    False
    """
    balance = 0
    for operation in operations:
        if operation > 0:  # deposit
            balance += operation
        elif operation < 0:  # withdrawal
            if balance < 0:
                return True
            balance -= operation
    return False
```
This function uses a loop to iterate through each operation in the list and update the balance accordingly. If at any time the FD (Fall Down) is detected, the function will return True; otherwise, it will return False.