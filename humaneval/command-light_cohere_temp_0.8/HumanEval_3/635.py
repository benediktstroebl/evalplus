Here's a self-contained Python function that solves the problem:
```python
def below_zero(operations):
    balance = 0
    for op in operations:
        if type(op) == int and op <= 0:
            balance -= op
        else:
            break
    return balance < 0
```
The function takes a list of operations as an input and iterates through each operation in the list. If an operation is an integer less than 0, it is subtracted from the balance. If the operation is zero or a withdrawal operation, it is subtracted from the balance. The function continues to the loop until a non-zero operation is encountered. If the balance of the balance ever becomes less than zero, the function will return True, indicating that the balance fell below zero at some point in the operations. If the loop completes without finding a negative operation, the function will return False, indicating that the balance never fell below zero.