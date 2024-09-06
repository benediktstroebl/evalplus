Here's the code that solves the markdown code block problem:
```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
    if balance < 0:
        return True
    return False
```
The function takes a list of operations as input and uses a loop to iterate over each operation. It starts with an initial balance of 0 and then adds each operation to the balance. When it detects that the balance is less than 0, it returns True. Otherwise, it returns False.