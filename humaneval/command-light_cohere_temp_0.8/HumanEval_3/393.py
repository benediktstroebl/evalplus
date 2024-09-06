Here's a self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    return balance < 0
```
This function takes a list of operations as an argument, where each operation is either a deposit or a withdrawal. It initializes a balance with 0 and iterates through each operation, adding the amount to the balance. When it detects that the balance is less than 0, it returns True, otherwise it returns False.