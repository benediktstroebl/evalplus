### Rolling Maximum in a Sequence
#### Problem: Find the rolling maximum in a sequence of numbers

The following Python function calculates the rolling maximum in a sequence of numbers. This function iterates over each element in the list and keeps track of the maximum element encountered so far.

```markdown
### Code
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of rolling maximum elements

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num  # Update max_so_far if current number is larger
        result.append(max_so_far)  # Append the maximum to the result list

    return result
```

### Example Usage
```markdown
# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(numbers)
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which calculates the rolling maximum in a sequence of numbers. It initializes `max_so_far` to negative infinity and iterates over each number in the input list. If a number is greater than or equal to `max_so_far`, it updates `max_so_far` to that number. Finally, it appends the current `max_so_far` to the result list and returns the result after iterating over all numbers. The script also includes an example usage of the `rolling_max` function to demonstrate its behavior.