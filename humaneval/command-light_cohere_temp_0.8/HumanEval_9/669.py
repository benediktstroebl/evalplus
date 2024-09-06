```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = List(numbers)  # convert list of strings to integers
    rolling_numbers = []
    while len(numbers) > 0:
        max_num = numbers[0]
        for num in numbers[1:]:
            if num > max_num:
                max_num = num
        rolling_numbers.append(max_num)
        numbers.remove(max_num)
    return rolling_numbers
```