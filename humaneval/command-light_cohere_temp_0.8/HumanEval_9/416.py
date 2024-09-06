```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns the list of rolling maximum elements found until the given moment in the sequence.
    The function uses the array notation to get the rolling max elements.
    Test case:
        input:
        numbers: list of integers, must be positive
    output:
        list of rolling maximum elements
    """
    numbers = [x for x in numbers if x > 0]
    return [x for x in numbers if x == max(numbers[i:])]
```