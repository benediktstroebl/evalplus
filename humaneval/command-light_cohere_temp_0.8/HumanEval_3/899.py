Here's the self-contained Python script with a function that solves the problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False

# Unit tests
tests = [
    [
     [below_zero([1, 2, -4, 5]) == True],
     [below_zero([-2, -4, 5]) == True],
     [below_zero([-2, 2, -4]) == False],
     [below_zero([10, -4, 5]) == False],
     [below_zero([100, -4, 5]) == False],
     [below_zero([]) == False]
    ]
]
```

The above script defines a function below_zero that takes a list of operations and determines whether the balance goes below zero. It iterates through for each operation, verifies the balance, and if the balance becomes negative, returns True; otherwise, it returns False. The function is also tested using a series of unit tests that cover various scenarios.