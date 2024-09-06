```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    >>> operations = [1, 2, -4, 5]
    Balance = 0
    for op in operations:
        Balance += op
    if Balance < 0:
        return True
    return False
    """

# Test the function
operations = [1, 2, -4, 5]
result = below_zero(operations)
print(result)  # Output: True

operations = [-1000, 2, -3, 1000]
result = below_zero(operations)
print(result)  # Output: False
```
This function uses a loop to iterate over each element in the list of operations. It adds up therolled operation to the balance and checks if the balance falls below zero. If the balance is indeed negative, the function returns True; otherwise, it returns False.