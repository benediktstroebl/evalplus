```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): List of integers to compute rolling max for.
        rolling_window (int): Size of the rolling max window.

    Returns:
        List[int]: List of length rolling_window containing the maximum elements encountered so far.
    """
    if not numbers or rolling_window <= 0:
        return []

    result = [float('-inf')] * rolling_window
    result[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(i - rolling_window + 1):
            if numbers[j] > numbers[i]:
                result[j] = numbers[i]

    return result
```

The provided code defines a function rolling_max that takes in a list of integers numbers and an integer rolling_window as input. It aims to create a new list where each element is the maximum value encountered in the preceding rolling_window interval within the original list.

Initially, the function handles edge cases where the input list is empty or the rolling window size is invalid. It then initializes a result list to hold the computed rolling maximum values, initially filled with -inf values. The first element of the result is set to the first element of the input list, numbers[0], as a starting point for the rolling maximum calculation.

The main iteration loop considers each element in numbers from index 1 onwards. It also goes back a rolling_window size distance from the current index, updating result elements as needed to retain the rolling maximum within the window.

Finally, the function returns the computed rolling maximum list. The provided example test case demonstrates how to use the function, and the expected output shows the result of applying the rolling maximum operation to a specific input.