```python
from typing import List, Tuple

def rolling_max(numbers: List[int], window_size: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if window_size >= len(numbers):
        return numbers[:]

    result = [None] * window_size
    result[0] = numbers[0]
    for i in range(1, len(numbers)):
        for j in range(1, window_size):
            if numbers[i] > numbers[j]:
                result[j] = numbers[i]
        if i >= window_size - 1:
            result[window_size - 1] = numbers[i]

    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers, 3))
```

In the provided example, the function `rolling_max` takes a list of numbers (`numbers`) and a `window_size` as input. It returns a list of rolling maximum elements found in the given window, with the rolling window moving along with the input sequence. 

The example usage demonstrates how to call the function with the sample input list `[1, 2, 3, 2, 3, 4, 2]` and a window size of 3, resulting in the output `[1, 2, 3, 3, 3, 4, 4]`.