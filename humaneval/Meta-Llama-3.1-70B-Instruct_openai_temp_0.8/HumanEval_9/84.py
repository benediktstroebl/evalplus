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
    if not numbers:
        return []

    max_value = numbers[0]
    rolling_max_values = [max_value]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
        rolling_max_values.append(max_value)

    return rolling_max_values


# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
expected_output = [1, 2, 3, 3, 3, 4, 4]
assert rolling_max(numbers) == expected_output, f"Expected {expected_output} but got {rolling_max(numbers)}"

print("Test passed. Rolling max values:", rolling_max(numbers))
```