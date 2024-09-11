```markdown
### Rolling Maximum Problem Solution

#### Problem Description
Generate a list of rolling maximum elements from a given list of integers.

#### Solution

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
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        # If the current number is greater than the last maximum, update the maximum
        if num > result[-1]:
            result.append(num)
        # Otherwise, keep the last maximum
        else:
            result.append(result[-1])

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation
The solution uses a simple iterative approach to keep track of the rolling maximum. It starts by initializing the result list with the first element of the input list. Then, it iterates over the input list starting from the second element. For each number, it checks if it is greater than the last maximum. If it is, it updates the maximum and adds it to the result list. Otherwise, it keeps the last maximum and adds it to the result list. Finally, it returns the result list.