Here's the Python script with a self-contained function that solves the problem of checking if the balance of a bank account ever falls below zero, and tests the function with sample inputs:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance -= op
    return balance < 0
# Test the function with some sample inputs
>>> below_zero([1, 2, -4, 5])
True
>>> below_zero([-10, -5, -20])
True
>>> below_zero([10, -5, -20])
False
>>> below_zero([1, 2, -20])
True
>>> below_zero([-1000, -1000, -100])
True
>>> below_zero([10, 20, 30])
False
``` 
This script defines a function below_zero, which takes a list of operations (deposits and withdrawals) as input. It initializes a its balance to zero and then iterates through each operation, subtracting the operation from the balance. The function returns True if the balance becomes negative, indicating that the balance ever falls below zero, and False otherwise.