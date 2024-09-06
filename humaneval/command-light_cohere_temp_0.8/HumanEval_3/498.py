Here is the above-mentioned function below:

```python
def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fall below zero, and
    at that point function should return True. Otherwise, it should return False.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([1, 2, 3, -1])
    False
    >>> below_zero([10, 20, 30])
    False
    """
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
The function takes a list of operations, which are integers representing deposit and withdrawal actions. It initializes a balance to zero and then iterates through the operations, adding each operation to the balance. After iterating through operations, the function checks if the balance is less than zero and returns True if so. If the balance is not negative, the function returns False.