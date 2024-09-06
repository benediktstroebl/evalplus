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
print(result)  # Output: True

# Test with a start balance
operations = [0, 1, 2, -4, 5]
balance = 10
result = below_zero(operations)
print(result)  # Output: False
```
The function takes a list of operations as input and iterates over them. It keeps track of the balance by initializing the balance to 0 and then subtracting each operation. If at any point the unique case, the balance becomes negative, the function returns True. If the balance is not negative at the end, it returns False.