Here's a Python script that uses a simple and efficient algorithm to solve the problem in linear time complexity.

```markdown
### Rolling Maximum Problem
#### Problem Statement
From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment in the sequence.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
            result.append(num)
        else:
            result.append(max_so_far)

    return result
```

#### Example Usage
```python
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script uses a dynamic programming approach to keep track of the maximum element seen so far. It iterates through the list of numbers, updating the `result` list and `max_so_far` variable accordingly, taking advantage of the fact that the rolling maximum of a sequence is determined by the maximum of the sequence so far. The time complexity of this solution is O(n), where n is the number of elements in the input list.