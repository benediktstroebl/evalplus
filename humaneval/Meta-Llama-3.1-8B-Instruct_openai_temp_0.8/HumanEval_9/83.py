### Rolling Maximum Elements
#### Solution
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    max_so_far = float('-inf')

    for num in numbers:
        # Update max_so_far if current number is greater
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
#### Explanation

The `rolling_max` function takes a list of integers as input and returns a list of rolling maximum elements. We initialize an empty list `result` to store the rolling maximum elements and `max_so_far` to keep track of the maximum element seen so far.

We iterate over the input list, updating `max_so_far` if the current number is greater, and append `max_so_far` to the `result` list at each step. This way, we generate the list of rolling maximum elements.

The time complexity of this solution is O(n), where n is the length of the input list, as we make a single pass over the list. The space complexity is also O(n), as we store the rolling maximum elements in the `result` list.