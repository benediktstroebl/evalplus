Here's a self-contained Python script that solves the rolling maximum problem:
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
    # Initialize an empty list to store the rolling maximum elements
    rolling_max_list = []

    # Initialize the current maximum element with the first number in the list
    current_max = numbers[0]

    # Append the current maximum to the list
    rolling_max_list.append(current_max)

    # Iterate over the rest of the numbers in the list
    for num in numbers[1:]:
        # Update the current maximum if the current number is greater
        if num > current_max:
            current_max = num

        # Append the current maximum to the list
        rolling_max_list.append(current_max)

    return rolling_max_list

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```