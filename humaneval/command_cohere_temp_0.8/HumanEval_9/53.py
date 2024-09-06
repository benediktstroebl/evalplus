Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0][1:rolling_window+1]) 
             for numbers in zip(numbers, numbers[1:])][:-rolling_window-1]
```

The function `rolling_max` takes in a list of integers `numbers` and an integer `rolling_window` as input and returns a list of integers, which is the rolling maximum element found in the sequence up to the given moment. The task is achieved through the use of zipper and list comprehensions to efficiently keep track of the rolling maximum value.  The given example in the docstring and the tests cases would be enough to catch the main logic and functionality of the function.