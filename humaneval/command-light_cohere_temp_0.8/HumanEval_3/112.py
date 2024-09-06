```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

# Test the function
# Operates on a list with mixed deposit and withdrawal values
# Returns True if balance falls below zero at any point, False otherwise
tests = [ [-4, 1, 2, -5, 3], [1, 2, -4, 5], [10, 20, 30, 40]]
for test_ops in tests:
    result = below_zero(test_ops)
    if result:
        print("YES")
    else:
        print("NO")
```