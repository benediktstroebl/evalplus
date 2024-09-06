```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

The `below_zero` function iterates through the list of `operations`, summing them to the running balance. If the balance ever goes negative, it immediately returns `True`. If the end of the operation list is reached and the balance is still non-negative, it returns `False`. This solution makes use of Python's strong typing and standard library typing module to make the function more readable and provide editor support. 

To test this function, you can call it with a list of operations and see if it returns the correct boolean values for the given scenarios. 
For example:
```python
# Test 1: Should return False
print(below_zero([1, 2, 3]))  # Output: False

# Test 2: Should return True
print(below_zero([1, 2, -4, 5]))  # Output: True
```

This script passes both test cases mentioned in the original problem and should correctly solve the given problem.