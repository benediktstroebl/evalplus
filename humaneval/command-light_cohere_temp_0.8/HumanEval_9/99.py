Here is a self-contained Python script that defines a function `rolling_max` solving the problem you provided:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [num for num, idx in sorted((v, i) for i, v in enumerate(numbers))
                    if numbers[i] > numbers[idx]]
```
The script provides a solution using a generator expression, where it creates a list of integers by iterating over the given list, and for each number, it checks if the current number is greater than the next element, which effectively is the rolling maximum found until the current moment.