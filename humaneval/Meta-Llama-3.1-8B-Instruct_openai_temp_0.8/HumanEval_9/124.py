### Rolling Maximum Problem Solution
#### Problem Statement
Given a list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum element found until given moment in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf')
    result = []

    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This solution iterates over the input list, keeping track of the maximum number encountered so far. For each number in the list, it checks if the current number is greater than the maximum so far. If it is, it updates the maximum so far and appends this new maximum to the result list. Otherwise, it appends the current maximum so far to the result list. This approach ensures that the rolling maximum is correctly calculated for each position in the input list.