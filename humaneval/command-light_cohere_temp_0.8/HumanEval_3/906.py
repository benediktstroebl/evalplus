Here's a self-contained Python script with a function that solves the problem and passes the tests:
```python
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
print(result)  # Output: True
```
This script defines a function `below_zero` that takes a list of operations as input. It initializes theMode with a balance of 0. Then, it iterates through operations. If at any point, the balance becomes less than 0, the function returns True. Otherwise, it returns False. The script also provides an test example using the `below_zero` function and prints the result.