```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.py_list = [1, 2, 3, 2, 3, 4, 2]
    return [x for x in numbers if x >= numbers[0] and x <= numbers[-1]]
```  This Python code defines a function `rolling_max` that takes a list of integers as input and generates a new list with the rolling maximum elements found in the original list. It creates a Python list `numbers.py_list` with the numbers [1, 2, 3, 2, 3, 4, 2], then iterates through this list using list comprehension and generates a new list `[x for x in numbers if x >= numbers[0] and x <= numbers[-1]]`, which contains the rolling maximum elements found until the first moment in the sequence.