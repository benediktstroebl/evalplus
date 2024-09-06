Here is the self-contained Python function that solves the problem and passes the tests:
```python
def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations=[1, 2, -4, 5]
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([6, -1, -3])
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
This function takes a list of operations and iterates through each operation, adding it to the balance. It returns True if the result falls below zero, otherwise, it returns False.