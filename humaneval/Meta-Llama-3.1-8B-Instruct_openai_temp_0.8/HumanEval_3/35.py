### Detecting Account Balance Below Zero

Below is a self-contained Python script that solves the problem.

```markdown
### Code

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if the balance of a bank account falls below zero at any point.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero, False otherwise.
    """
    balance = 0  # Initialize balance to zero
    for operation in operations:
        balance += operation  # Update balance after each operation
        if balance < 0:  # Check if balance falls below zero
            return True
    return False  # Return False if no operation caused balance to fall below zero


### Example Use Cases

print(below_zero([1, 2, 3]))  # False
print(below_zero([1, 2, -4, 5]))  # True
```

### Explanation

This script defines a function `below_zero` that takes a list of operations as input. It initializes the balance to zero and iterates over the operations. After each operation, it checks if the balance falls below zero. If it does, the function immediately returns `True`. If no operation causes the balance to fall below zero, the function returns `False`.