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
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_max_list = [max_so_far]

    # Iterate through the list starting from the second element
    for num in numbers[1:]:
        # Update the maximum if the current number is larger
        max_so_far = max(max_so_far, num)
        # Append the current maximum to the result list
        rolling_max_list.append(max_so_far)

    return rolling_max_list


# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This script defines the `rolling_max` function, which takes a list of integers as input and returns a list of rolling maximum elements. It initializes the maximum so far with the first element of the input list and then iterates through the rest of the list, updating the maximum and appending it to the result list whenever it encounters a larger number. Finally, it includes an example usage of the function.