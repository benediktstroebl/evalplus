```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False

# Unit tests
operations = [1, 2, -4, 5]
test_below_zero = below_zero(operations)
assert test_below_zero == True  # Should be True

operations = [1, 2, 3, -5, 6]
test_below_zero = below_zero(operations)
assert test_below_zero == False  # Should be False
```

This code defines a function `below_zero` that checks if the balance of an account falls below zero after applying a list of operations. It uses a basic iterative approach to calculate the balance and check for conditions. The tests ensure that the function is correctly implementing the desired behavior.