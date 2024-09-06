Here is a Python script with a self-contained function that solves the problem of finding the rolling maximum element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements found in the given sequence.
    Args:
    numbers: List[int], a list of integers.
    Returns: a list of rolling maximum elements, ordered sequentially.
    """
```

def rolling_max(numbers: List[int]) -> List[int]:
    res = []
    while True:
        if len(numbers) == 0:
            break
        current_max = numbers[0]
        for num in numbers[1:]:
            if num > current_max:
                current_max = num
        res.append(current_max)
    return res
```
This script defines a function `rolling_max` that takes a list of integers as an argument and returns a list of the rolling maximum elements. The function uses a while loop, starting from the first element, and compares each element with the current maximum until it encounters a smaller number. The rolling maximum is then updated and added to the result list.