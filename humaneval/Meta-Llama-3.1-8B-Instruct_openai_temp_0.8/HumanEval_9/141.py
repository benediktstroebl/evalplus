### Rolling Maximum Problem Solution
#### Python Script
```markdown
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
    if not numbers:
        return []

    result = [numbers[0]]
    max_so_far = numbers[0]

    for num in numbers[1:]:
        if num >= max_so_far:
            result.append(num)
            max_so_far = num
        else:
            result.append(max_so_far)

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))
```
This Python script uses a simple iterative approach to maintain a running maximum value as it iterates through the input list. It keeps track of the maximum value seen so far and appends this to the result list as it iterates over the numbers. If a number is greater than the current maximum, it updates the maximum and appends this new maximum to the result list. Otherwise, it simply appends the current maximum to the result list. The result is a list of "rolling maximum" values corresponding to each position in the input list.