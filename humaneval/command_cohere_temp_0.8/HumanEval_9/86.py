```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

    Args:
        numbers (List[int]): The list of integers.
        rolling_window (int): The rolling window size.

    Returns:
        List[int]: The list of rolling maximum elements.
    """

    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('-inf')] * rolling_window

    rolling_maxes = [float('-inf')] * rolling_window
    rolling_maxes[0] = numbers[0]

    for i in range(1, len(numbers)):
        for j in range(rolling_window - 1):
            if numbers[i] > rolling_maxes[j]:
                rolling_maxes[j + 1:] = rolling_maxes[j:] + [numbers[i]]
                rolling_maxes[j] = numbers[i]

    return rolling_maxes
```

The algorithm for the above function operates as Follows:
1. Begin with `rolling_maxes` as a list of `rolling_window` elements, all initialized to negative infinity. 
2. The first element of the list is always the maximum, so set it to the first element of `numbers`.
3. For each subsequent element in `numbers`, update the `rolling_window`-sized subarray of `rolling_maxes` that
    contains the previous maximum to be the new element.

This algorithm takes advantage of the fact that we only need to update a small subarray of `rolling_maxes` 
whenever we encounter a new element in `numbers`. It follows a window-based approach, allowing us to compute 
the rolling maximum efficiently using only a few operations per step, regardless of the size of `numbers`. 

I hope this solution provides an efficient approach to compute the rolling maximum while maintaining a manageable code size. Let me know if you would like to discuss any aspect of this solution or explore additional ideas further. Trà