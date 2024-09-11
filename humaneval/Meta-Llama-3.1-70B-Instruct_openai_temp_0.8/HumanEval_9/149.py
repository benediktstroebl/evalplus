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

    max_elements = [numbers[0]]
    current_max = numbers[0]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_elements.append(current_max)

    return max_elements


# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this script, the function `rolling_max` takes a list of integers as input and returns a new list where each element at index `i` is the maximum of all elements up to index `i` in the original list.

The function iterates through the input list, keeping track of the current maximum value. If a new maximum is found, it updates the current maximum and appends it to the result list. Otherwise, it appends the current maximum to the result list.

The script also includes an example usage of the function, demonstrating how to call it with a sample list of numbers and print the result.