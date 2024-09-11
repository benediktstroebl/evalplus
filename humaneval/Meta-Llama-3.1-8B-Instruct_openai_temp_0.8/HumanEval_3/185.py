### below_zero Function in Python
Below is a Python function that meets the requirements. This function iterates over the list of operations, keeping track of the current balance. As soon as it encounters a balance that is less than zero, it immediately returns True. If it checks all operations without entering the function early, it returns False.

```python
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detects if at any point the balance of account falls below zero.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations on a bank account.

    Returns:
    bool: True if the balance of account falls below zero, False otherwise.
    """
    balance = 0  # Initialize the balance to zero
    for operation in operations:  # Iterate over each operation
        balance += operation  # Update the balance
        if balance < 0:  # Check if the balance is below zero
            return True  # Return True if the balance is below zero
    return False  # Return False if all operations didn't put the balance below zero

# Test the function
print(below_zero([1, 2, 3]))  # Should print False
print(below_zero([1, 2, -4, 5]))  # Should print True
```

This function uses a simple iterative approach to keep track of the balance and return as soon as it encounters a negative balance. It has a time complexity of O(n), where n is the number of operations, because it makes a single pass over the list. The space complexity is O(1), because it uses a constant amount of space to store the balance and the operation being processed.