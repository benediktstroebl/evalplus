Here's the self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
```
The function checks each operation in the operations list and updates the balance accordingly. If the balance falls below zero, the function returns True, otherwise, False. The function is designed to be self-contained, and it can be used directly with test cases.