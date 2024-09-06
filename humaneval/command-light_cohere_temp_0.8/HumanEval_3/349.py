Here's a Python script that includes a self-contained function, `below_zero`, which solves the problem you provided:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    # Function to check if the balance of the account ever falls below zero
    # starting from an initial balance of 0
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance += op
    return False

# Test the function
# Test with list of operations, starting from an initial balance of 0
test_cases = [
    [0, 1, 2, -4, 5],
    [-100, 101, 102, -103, 105],
    [0, -10, -5, -20],
    [10000, -1000, -100]
]

for test_case in test_cases:
    actual = below_zero(test_case)
    print(f"{test_case} : {actual}")
```

The `below_zero` function checks if the balance of the account ever falls below zero, starting from an initial balance of 0. If the balance ever becomes negative, the function will return `True`, otherwise, it will return `False`.