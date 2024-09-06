Here's the self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation <= balance:
            balance -= operation
        else:
            return True
    return False
```

This function takes a list of operations, where each operation could be a deposit or withdrawal. It initializes a balance to zero and then iterates through the operations. At each iteration, if the operation is less than the current balance, it subtracts the operation from the balance. If the operation is greater than the balance, it returns True, indicating that the balance fell below zero.