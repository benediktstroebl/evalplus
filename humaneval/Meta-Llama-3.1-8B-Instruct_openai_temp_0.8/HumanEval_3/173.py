```markdown
### Below Zero Balance Detection

This script detects if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

#### Code

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if the balance of a bank account falls below zero at any point given a list of deposit and withdrawal operations.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over the operations
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True if the balance falls below zero
    return False  # Return False if the balance does not fall below zero

# Test cases
print(below_zero([1, 2, 3]))  # Output: False
print(below_zero([1, 2, -4, 5]))  # Output: True
```

#### Explanation

This script defines a function `below_zero` that takes a list of integers representing deposit and withdrawal operations. It initializes the balance to zero and iterates over the operations, updating the balance and checking if it falls below zero. If the balance falls below zero at any point, the function returns True. If the balance does not fall below zero after iterating over all operations, the function returns False.

#### Time Complexity

The time complexity of this script is O(n), where n is the number of operations, because it iterates over the operations once. The space complexity is O(1), because it uses a constant amount of space to store the balance.