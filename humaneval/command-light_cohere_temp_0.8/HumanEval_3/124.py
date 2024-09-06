Here's a self-contained Python script that solves the problem you described:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test cases
operations1 = [1, 2, -4, 5]
operations2 = [1, 2, 3]

result1 = below_zero(operations1)
result2 = below_zero(operations2)

print("Result 1:", result1)
print("Result 2:", result2)
```

This script defines a function `below_zero` that checks if the balance of a bank account falls below zero after applying a series of deposit and withdrawal operations. The balance is initialized to 0, and the loop iterates through each operation in the `operations` list. If at any point the well condition is met, the function returns `True`, otherwise, it returns `False`. The script also provides two test cases, and the function is called with those test cases.