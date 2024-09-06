```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:
            balance += operation
        elif operation < 0:
            balance -= operation
    return balance < 0
# Example usage
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)
``` 
This code defines a function `below_zero` that checks if the balance of a bank account falls below zero after processing a list of operations. It uses a's simple strategy where it maintains the balance and checks if the balance becomes negative. The script also provides an test case to demonstrate the usage of the function.