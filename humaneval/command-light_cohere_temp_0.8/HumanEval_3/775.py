```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op <= 0:
            return True
        balance += op
    return False
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
``` 
This function will accurately detect whether the balance of the account ever falls below zero and return the appropriate result.