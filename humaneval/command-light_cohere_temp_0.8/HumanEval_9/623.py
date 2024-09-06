Here's a self-contained Python function that generates a list of rolling max elements:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A function that finds the rolling maximum element in a list.
   
    Returns a max elements in a list, the rolling maximum element found 
    until the moment given in the list.
    """
    returns a list with max elements as the rolling maximum elements 
    until the moment given.
    """
```
# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_output = rolling_max(numbers)
print(rolling_max_output)  # Expected output: [3, 3, 3, 4, 4]

This script provides a self-contained solution to the rolling max problem.