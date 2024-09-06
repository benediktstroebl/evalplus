```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
        if balance < 0:
            return True
    return False
# Test the function
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
```
This script defines a function below_zero that checks if any operation in a list of operations would make the balance of an account go below zero. The function iterates through each operation in the list and updates the balance accordingly. If the balance becomes negative, it returns True, otherwise, it returns False.

The test code provided then calls the below_zero function with a sample list of operations and prints the result, which should be True.