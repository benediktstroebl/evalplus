```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling 
    maximum elements found until the given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    max_numbers = [x for x in numbers if numbers.count(x) == 1]
    rolling_max_numbers = [max(max_numbers) + 1 for max_numbers in max_numbers]
    return rolling_max_numbers
```