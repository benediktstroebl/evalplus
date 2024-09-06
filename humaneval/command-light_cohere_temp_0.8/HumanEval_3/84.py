```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
``` 
This code defines a function below_zero that checks whether the balance of an account falls below zero after processing a list of operations. The balance variable keeps track of the current balance and iterates through the operations.