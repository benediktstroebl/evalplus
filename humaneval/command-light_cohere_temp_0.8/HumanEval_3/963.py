Here's the provided Python script that includes the self-contained function below_zero, which solves the problem you described:
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
operations2 = [100, 200, -20, 300]

print(below_zero(operations1))  # Output should be True
print(below_zero(operations2))  # Output should be False
```

The above code defines a function below_zero that takes a list of operations and returns a boolean value indicating whether the balance of the account falls below zero at any point. The balance variable is initialized to zero, and the loop iterates over each operation in the list. If the balance becomes negative, the function returns True. Otherwise, it continues with the next iteration.