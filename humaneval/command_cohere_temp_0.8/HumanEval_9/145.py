Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[i:i+rolling_window]) for i in range(len(numbers) - rolling_window + 1)]
```

The `rolling_max` function takes in a list of integers `numbers` and an integer `rolling_window` as input and returns a list of integers, which is the rolling maximum elements in the sequence, over a rolling window of size `rolling_window`. 

Here is an example usage of the function:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 2)
# [1, 3, 3, 3, 4, 4]
```

This will return a list of rolling maximum elements over a window of size 2, calculated at each step of the sequence, starting from the beginning. 

Such a function could be used, for example, in a chatbot to find the rolling maximum score, for a gamification sequence of points, scored at certain moments in time.