Here's the self-contained Python function to solve the problem you've outlined: 

```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op <= 0:
            balance -= op
        else:
            break
    return balance < 0
```

This function iterates over the operations list and for each operation, if it's a negative number, it will reduce the balance ( think of a deposit operation), and if it's non-negative, it will break out of the loop since the operation is a withdrawal/deposit operation, which would make the balance non-negative.

This function is self-contained and will correctly determine if the balance falls below zero.