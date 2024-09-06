Here's the self-contained Python function that solves the problem you described: 

```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```

This function iterates through the list of operations, continuously decrementing the balance. It will return True if at any point the balance falls below zero, and False otherwise.