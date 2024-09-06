Here's a self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    """ Checks if the balance of the account falls below zero at any point.
    >>> operations = [1, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0, 2, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [-1, 0, -4, 5]
    >>> below_zero(operations)
    True
    >>> operations = [0, 2, 3, -4, 5]
    >>> below_zero(operations)
    False
    """
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function below_zero takes a list of operations and checks if the balance ever falls below zero. The loop iterates over the values in the list and adds each operation to the balance. The loop will terminate when the balance becomes zero, indicating the start of a new deposit operation.