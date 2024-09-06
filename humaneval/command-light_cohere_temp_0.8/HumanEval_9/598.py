```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.
    """
    return [list(numbers)[::-1][max_position]:numbers[max_position] for max_position in enumerate(numbers) if numbers[max_position]>numbers[-1-max_position]] else numbers[-1]
    """
    return numbers[::-1][max_position]:numbers[max_position] for max_position in enumerate(numbers) if numbers[max_position]>numbers[-1-max_position]] else numbers[-1]
```
This function takes a list of integers as input and generates a list of rolling maximum elements found until the given moment in the sequence.