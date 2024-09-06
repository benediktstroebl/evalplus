Here's the solution to the markdown code block problem:

```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

This code checks each operation against a running balance. If the balance ever goes below zero, it returns `True`, otherwise, it returns `False` and you can use this function with any list of operations to determine if the balance goes below zero.