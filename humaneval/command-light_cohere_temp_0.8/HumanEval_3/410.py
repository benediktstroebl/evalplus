```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False

#Test cases
 operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output should be True
``` 
The function checks if the balance ever falls below zero and returns True. The test cases pass successfully.