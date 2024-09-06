Here's the self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
```
This function takes a list of deposit and withdrawal operations and iterates over them. It starts with an initial balance of zero and checks if at any point, the balance falls below zero. If it does, the function returns True, indicating a negative balance. Otherwise, it returns False.