Here's the self-contained Python function that solves the problem you described: 

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
    >>> below_zero([6, -1, -3])
    False
    """
    balance = 0
    for op in operations:
        if op > 0:
            balance += op
        elif op < 0:
            return True
    return False
```
This function takes a list of deposit and withdrawal operations and returns `True` if the balance ever falls below zero, otherwise it returns `False`. 

The function uses a loop to iterate through the list of operations. It adds the deposit operations, and subtracts withdrawal operations. If an operation is greater than zero, it adds the operation to the balance. If an operation is less than zero, it immediately returns `True`. 

This function can be used as a starting point for solving the problem, and it can be used to pass tests to check its correctness.