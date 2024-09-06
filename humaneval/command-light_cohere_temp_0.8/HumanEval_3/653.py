Here is a self-contained Python function that solves the problem you provided:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

The function uses a loop to iterate over each operation in the list. Then it adds the particular operation to the balance and checks if the balance went below zero. If the balance goes below zero, the function returns `True`. Otherwise, it returns `False`.