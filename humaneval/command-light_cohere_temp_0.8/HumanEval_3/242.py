Here's the code:
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
# Test 1
print(below_zero([1, 2, -4, 5]))  # Output: True

# Test 2
print(below_zero([1, 2, 3]))    # Output: False

# Test 3
print(below_zero([10, 5, -10])) # Output: True

# Test 4
print(below_zero([10, 5, -1]))  # Output: True
```

This script defines a function `below_zero` that takes a list of operations and checks if the balance of the account ever falls below zero. The function iterates through each operation, and if the balance becomes negative, it returns `True`. Otherwise, it continues iterating and returns `False`.