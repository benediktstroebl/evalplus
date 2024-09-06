Here's a self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op < 0:
            balance -= op
        else:
            break
    return balance < 0
```
This function takes a list of operations as input and iterates through each operation in the list. The function simulates the balance of the account and returns True if, at any point, the balance of the account falls below zero. It ensures the balance is maintained as you perform deposits and withdrawals by checking if an operation is negative, subtracting it from the balance, and breaking out the loop if the operation is non-negative.