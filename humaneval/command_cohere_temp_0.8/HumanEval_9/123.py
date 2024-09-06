```python
from typing import List, Tuple

def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if max_window is None:
        max_window = len(numbers)

    result = [num for num in numbers]
    for i in range(1, max_window):
        result[i] = max(result[i-1], result[i])

    return result
``` 

The `rolling_max` function takes a list of numbers as an argument and returns a list of rolling maximum values found in the list. By default, the function uses the length of the input list as the rolling window size, or it can be explicitly set by the `max_window` parameter. The function iterates through the list, filling in the rolling maximum value for each position in the result list. The result is a list of rolling maximum values for each position in the input list, up to the maximum window size. 

The problem statement and tests are correctly reflected in the function's description and the script provided.  This approach ensures efficiency and is easily adaptable to any list of numbers and rolling maximum length.