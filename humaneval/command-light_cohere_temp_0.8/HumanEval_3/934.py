```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
# Tests
# Operations
operations = [1, 2, -4, 5]
# Check if the balance goes below zero
result = below_zero(operations)
print(result)  # Output: True
# Check if a single operation causes below-zero
result = below_zero([1])
print(result)  # Output: False
``` 
The function below_zero uses a loop to iterate over the operations in the list operations. After each operation is the balance is incremented by the operation, and the function checks if the balance has gone below zero. The function returns True if the balance has gone below zero, and False otherwise.