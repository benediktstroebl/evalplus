```Python
from typing import List
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if op < 0:
            balance -= op
        else:
            break
    return balance < 0
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
``` 
This script defines a function below_zero that takes a list of operations as input. It iterates over each operations and checks if any operation is a negative value, in which case it will subtract the operation from the balance, and if no operations are non-positive, it will return True. The function returns True as long as the balance will be less than 0 after iterating through the operations.