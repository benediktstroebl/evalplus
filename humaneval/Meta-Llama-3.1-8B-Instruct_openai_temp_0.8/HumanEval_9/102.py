### Rolling Maximum Calculator
#### Problem Statement
Given a list of integers, generate a list of rolling maximum elements found until each moment in the sequence.

#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers: A list of integers.

    Returns:
        A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(max(result[-1], num))
    
    return result

# Example Usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to calculate the rolling maximum by keeping track of the maximum element seen so far. The example usage demonstrates how to use this function with a sample list of numbers.