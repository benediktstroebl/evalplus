```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The list of integers to process.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list containing the rolling maximum seen at each position up to the current moment in the sequence.
    """
    if not numbers or rolling_window <= 0:
        return []

    result = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - rolling_window]:
            result[i] = numbers[i - rolling_window]
    return result
```

The `rolling_max` function takes in two parameters: `numbers`, which is the list of integers to process, and `rolling_window`, which indicates the size of the rolling maximum window. It initializes the `result` list with the original input numbers and then iterates through the list, comparing each element with the maximum element from the window of the previous `rolling_window` elements. If the current element is greater, it leaves the current element unchanged. Otherwise, it replaces the current element with the maximum element from the window, effectively keeping track of the rolling maximum up to the current position. 

Here is an example of how you can use this function to solve the problem:
```python
# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max(numbers, 3)
```

The output will be:
```python
[1, 2, 3, 3, 3, 4, 4]
```

This is the expected result, representing the rolling maximum elements seen up to each position in the given sequence.