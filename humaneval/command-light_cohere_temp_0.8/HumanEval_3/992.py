```Python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation < 0:
            balance -= operation
        else:
            break
    return balance < 0

# Test cases
# Start with balance at 0
initial_balance = 0
test_operations = [1, 2, -4, 5]
result = below_zero(test_operations)
assert result == True, "Operations do not go below zero"

# Test with starting balance not 0
initial_balance = -10
test_operations = [1, 2, -4, 5]
result = below_zero(test_operations)
assert result == True, "Operations do not go below zero"

# Test with balance 0, but no operations
test_operations = []
result = below_zero(test_operations)
assert result == False, "Operations should not reach zero"

# Test with balance above 0
initial_balance = 10
test_operations = [1, 2, -4, 5]
result = below_zero(test_operations)
assert result == True, "Operations go below zero"
```