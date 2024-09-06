Here's the self-contained Python function that solves the problem:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
```
This function takes a list of deposit and withdrawal operations as input. It initializes a to an initial balance of 0. It then iterates through operations and checks if at any point, the balance falls below zero. If so, it returns True, otherwise, False. at returns False.

Note that this function is self-contained, meaning it can be fully understood and implemented within the function itself without the need for external input or calls to other functions. This makes it design simple, clear, and easy to maintain.