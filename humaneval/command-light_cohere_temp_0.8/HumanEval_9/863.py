```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements.
    >> The generate a rolling maximum by summing the current maximum and current element, 
    and updating the current maximum accordingly.
    """
    use the general sorting to sort the list of numbers.
    The rolling maximum starts from an number in the list, 
    which is the largest and reverts the list and starts anew.
    >> return: list of rolling maximum elements
    """
    numbers.sort()
    roll = sorted(numbers)[::-1]
    rolling_max = [0]
    while roll[-1] < numbers[-1]:
        rolling_max.append(roll[-1] + roll[-2])
        roll = roll[:-2] + roll[1:]
    return roll[::-1]
```