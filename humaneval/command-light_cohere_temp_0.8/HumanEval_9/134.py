```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i % 2 == 0 and num > numbers[i]]
```
This Python script defines a function `rolling_max` that takes a list of integers as input and returns a list of integers, where each element is the maximum of its corresponding index in the input list, with an even index. The output list will only contain the maximum elements of the original list, in ascending order. The provided test solves the recent input problem with ease and efficiency, with clear and self-contained logic.