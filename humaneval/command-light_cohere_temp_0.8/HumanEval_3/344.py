```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if balance < 0:
            return True
        balance -= operation
    return False
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True
```
This solution defines a function below_zero that takes a list of operations (deposit and withdrawal) as an argument. The function loops through the to simulate the account balance, and for each operation, it checks if the balance falls below zero. If it does, the function returns True, indicating that at least one operation caused the balance to go below zero. If the balance remains non-negative throughout the loop, the function returns False, indicating that no operations caused the balance to go below zero.