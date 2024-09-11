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

    rolling_maxima = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_maxima.append(current_max)

    return rolling_maxima


# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function that takes a list of integers as input and returns a list of rolling maximum elements. The function iterates over the input list, keeping track of the current maximum element and appending it to the `rolling_maxima` list at each step. The script also includes a docstring with an example usage and a test case in the `if __name__ == "__main__":` block.