```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
```

The script introduces an iterative approach to account summing up the operations in the list, and at the very end checks if the final balance is less than zero. As a result, it correctly returns True for examples like `below_zero([1, 2, -4, 5])` and `below_zero([1, 2, 3])`, and `False`.  This way it satisfies the test cases provided in the prompt and correctly solves the problem.