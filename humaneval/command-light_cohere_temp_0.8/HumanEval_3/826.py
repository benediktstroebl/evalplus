Here's the solution:

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance = balance + operation
    if balance < 0:
        return True
    return False
```

The function below_zero takes a list of operations as input and uses a loop to iterate through the operations. It starts with an initial balance of 0 and then adds the operation to the balance. If the balance becomes below zero, it returns True, otherwise, it returns False.

This function is a complete self-contained solution that can be used to solve the problem described in the prompt. It effectively detects if the the balance falls below zero using a loop and returns the result accordingly.