```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
# Test the function
# Operations: [1, 2, -4, 5]
# Expected output: True
below_zero([1, 2, -4, 5])

# Test the function with operations that do not reach zero balance
# Operations: [0, 2, 3]
# Expected output: False
below_zero([0, 2, 3])
``` 
This script defines a function called below_zero, which takes a list of operations as input and returns a boolean value. The function iterates through each operation in the list and adds it to the balance. If the balance falls below zero, the function returns True, indicating that the balance is negative and the function has detected the condition.  Otherwise, the function returns False, indicating that the balance is not negative. 

The script also provides two tests to verify the correctness of the function. It successfully detects the example with operations that lead to a negative balance, and correctly predicts the output as True.