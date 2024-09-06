Here is a Python script with a self-contained function that solves the problem:

```python
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        if balance < 0:
            return True
        balance -= op
    return False


# Testing the function
deposit = [1, 2, -4, 5]
with_balance = 0
result = below_zero(deposit)
print(result)

with_balance = -10
result = below_zero([1, 2, -4, 5])
print(result)
```

The code provides a method that checks a list of operations for withdrawals and deposits to a starting balance. It makes use of a for loop to iterate through each operation, if the balance falls below zero, it returns True. The balance is updated by the value of each operation, if the balance becomes zero or greater than zero, the function returns False, which means no operations caused the balance to go below zero.