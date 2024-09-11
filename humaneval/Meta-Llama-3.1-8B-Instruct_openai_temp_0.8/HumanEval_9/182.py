Here is the Python script that solves the problem:

```markdown
# Rolling Maximum Problem
========================

This script generates a list of rolling maximum elements found until a given moment in the sequence.

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    current_max = numbers[0]
    
    for num in numbers[1:]:
        if num >= current_max:
            result.append(num)
            current_max = num
        else:
            result.append(current_max)
    
    return result
```

### Example Usage:

```python
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. It uses a simple iterative approach to keep track of the current maximum and the result list. The example usage demonstrates how to use the function with a sample list of numbers.