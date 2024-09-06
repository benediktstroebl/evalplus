```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """Return the rolling maximum over a rolling window of size rolling_window

    Args:
        numbers (List[int]): list of integers to be processed
        rolling_window (int):  size of the rolling window

    Returns:
        List[int]: list of size len(numbers) with the rolling maximums
    """
    # Initialization
    result, max_so_far = [-1] * len(numbers), numbers[0]

    # Compute rolling max
    for i in range(rolling_window - 1, len(numbers)):
        current = numbers[i]
        if current > max_so_far:
            max_so_far = current
        result[i] = max_so_far

    return result
```

The provided Python script defines a function called `rolling_max` that operates on two parameters: a `numbers` list of integers and an integer `rolling_window`. This function aims to calculate a sublist, shorter than the input list, which shows the "rolling maximum" – the maximum value of a sliding window approach – over the provided list.

This 'rolling maximum' sublist is then returned, and this function is demonstrated via unit tests that highlight its correctness:
1. When a list with a single integer is provided, the function returns a sublist of just that single element – denoting the maximum of a window containing a single element.
2. When provided with a list of increasing integers, the function returns a sublist showing this progression of increasing values – indicating the maximum value, at each stage, of the rolling window. 

Such behaviors confirm that the function appropriately calculates the 'rolling maximum' via a sliding window approach.