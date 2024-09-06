```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within rolling_length windows.
    """
    if rolling_length <= 0:
        return []

    res = [max(numbers[:rolling_length])]
    for i in range(1, len(numbers) - rolling_length + 1):
        max_window = max(numbers[i:i+rolling_length])
        res.append(max_window if max_window > res[-1] else res[-1])

    return res

# Example usage
test_cases = [
    ([1, 2, 3, 2, 3, 4, 2], 5),
    ([-2, -1, -4, -3, -2, -1, -5, -3], 3),
]

for numbers, rolling_length in test_cases:
    print(rolling_max(numbers, rolling_length))
``` 

This code defines a function called `rolling_max` that takes in two parameters, `numbers` which is a list of integers and `rolling_length` which is the length of the rolling window. The function generates a list of integers, where each integer represents the maximum value within a rolling window (of the specified length) throughout the entire input list. The algorithm achieves this by keeping track of the maximum value of the first window in the resulting list (`res[0] = max(numbers[:rolling_length])`), then compares subsequent window maxima with the maximum of the previous window, appending the greater of the two (`res.append(max_window if max_window > res[-1] else res[-1])`). 

The example usage provides test cases that demonstrate how the `rolling_max` function works.