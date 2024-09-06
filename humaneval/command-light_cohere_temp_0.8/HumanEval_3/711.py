Here is a self-contained Python script that defines a function below_zero that checks whether the balance of a bank account falls below zero, given a list of deposit and withdrawal operations:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        if operation > 0:  # deposit
            balance += operation
        elif operation < 0:  # withdrawal
            if balance < 0:
                return True
            balance -= operation
    return balance < 0

# Test the function with test cases
>>> below_zero([1, 2, -4, 5])
True
>>> below_zero([1, 2, 3])
False
>>> below_zero([4, -3, -5])
True
>>> below_zero([5, -5, -5])
False
``` 
This function uses a simple algorithm to iterate through the list of operations, and at each iteration, it either adds the operation to the balance if it's a deposit, or subtracts the operation from the balance if it's a withdrawal. The function continues this until the balance is less than zero, at which point, the function returns True, indicating that the balance has fallen below zero.