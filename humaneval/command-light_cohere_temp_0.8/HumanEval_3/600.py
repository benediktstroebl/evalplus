```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
    return balance < 0
```
The function takes a list of operations as input and initializes the balance variable to zero. It then iterates over each operation in the list, adding its value to the balance. After iterating over all operations, the function checks if the balance is less than zero and returns True if the condition is met, otherwise, it returns False.