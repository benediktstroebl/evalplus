### Rolling Maximum in a Sequence
#### Problem Description
Generate a list of rolling maximum elements found until a given moment in the sequence.

#### Solution
```markdown
### Code
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
    max_so_far = float('-inf')  # Initialize max_so_far as negative infinity
    result = []  # Initialize an empty list to store the result

    for num in numbers:  # Iterate over the input list
        if num > max_so_far:  # If current number is greater than max_so_far
            max_so_far = num  # Update max_so_far
        result.append(max_so_far)  # Append max_so_far to the result list

    return result  # Return the result list
```

#### Example Usage
```python
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, keeping track of the maximum element found so far. The maximum element is appended to the result list at each iteration. Finally, the function returns the result list.