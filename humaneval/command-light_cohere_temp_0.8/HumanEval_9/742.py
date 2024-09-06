```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until a given moment
    in the sequence.
    Parameters: numbers: List[int]
    Returns: List[int]
    """
    numbers = List(sorted(numbers))
    seen = set()
    result = []
    while len(numbers) > 0:
        num = numbers.pop(0)
        if num > 0 and num in seen:
            seen.add(num)
        result.append(num)

    return result
```
This function takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence. The function uses a provided approach to solve this problem, which involves iterating through the list, maintaining a set of seen numbers, and appending the maximum number of each iteration to the result list.