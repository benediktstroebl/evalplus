```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers to compute rolling maximum for.
        rolling_window (int): Window size to compute the rolling maximum for.

    Returns:
        List[int]: List of maximum elements seen until the current window in the sequence.
    """
    
    if not numbers or not rolling_window:
        return []

    rolling_maxes = [numbers[0]]

    for i in range(1, len(numbers)):
        max_element = numbers[i]
        for j in range(i - rolling_window + 1, i):
            if numbers[j] > max_element:
                max_element = numbers[j]

        rolling_maxes.append(max_element)

    return rolling_maxes

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3
result = rolling_max(numbers, rolling_window)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

The `rolling_max()` function takes in two arguments: a `List[int]` called `numbers` and an `int` called `rolling_window`. The function generates a list of maximum elements seen within the current window in the sequence. To achieve this, it starts with an empty list to store the rolling maximum elements and initializes the first element of the list to be the first element of the input `numbers`. It then iterates through the rest of the input list, comparing each element with the current maximum element stored and updating it if a larger element is found. After each update, the updated maximum element is appended to the list of rolling maximum elements. The function returns the list containing the maximum elements seen within the defined window for the input sequence. 

The output of the provided example usage is `[1, 2, 3, 3, 3, 4, 4]`, which represents the rolling maximum elements seen in windows of size 3 for the given input sequence `[1, 2, 3, 2, 3, 4, 2]`.