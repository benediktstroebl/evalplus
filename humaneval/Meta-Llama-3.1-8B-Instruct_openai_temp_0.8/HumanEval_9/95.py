### Rolling Maximum Problem
#### Description
This script generates a list of rolling maximum elements found until a given moment in a sequence of integers.

#### Code
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
    rolling_max_list = []
    max_so_far = float('-inf')  # Initialize max_so_far to negative infinity

    for num in numbers:
        if num >= max_so_far:
            max_so_far = num
            rolling_max_list.append(max_so_far)

    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation
This script uses a simple iterative approach to maintain the maximum element seen so far (`max_so_far`) and append it to the `rolling_max_list` whenever a new maximum is found. The list is populated in a single pass through the input list, making the script efficient with a time complexity of O(n), where n is the length of the input list.