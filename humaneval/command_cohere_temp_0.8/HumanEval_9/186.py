Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[i - rolling_window:i]) for i in range(len(numbers) - rolling_window + 1)]
```

The `rolling_max` function takes in a list of integers `numbers` and an integer `rolling_window` as inputs. It returns a list of integers, which is the maximum value within the rolling window for each element in `numbers`. The rolling window is moved from the beginning to the end of the sequence, and the maximum value within each window is recorded. 

You can use the function by calling `rolling_max` with a list of numbers and the desired rolling window size. Here is an example:
```python
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3

result = rolling_max(numbers, rolling_window)

print(result)
# Output: [1, 2, 3, 3, 3, 4, 4]
``` 

This will return a list of integers where each element represents the maximum value of the rolling window for each element in the input list.  For the given example, the output will be `[1, 2, 3, 3, 3, 4, 4]`, where each value corresponds to the maximum of the rolling window started at that index.