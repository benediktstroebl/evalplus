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
# We need to test it with negative numbers as well as a combination that would result in a balance below zero
test_below_zero = below_zero([1, 2, -4, 5])
assert test_below_zero == True
test_below_zero = below_zero([1, 2, -3])
assert test_below_zero == True
test_below_zero = below_zero([0, -1, 2])
assert test_below_zero == False
``` 
The function below_zero takes a list of operations, and iteratively processes each operation in the list, checking if the balance of the account falls below zero. The function returns True if the balance becomes negative, and False if it remains non-negative after processing all operations.