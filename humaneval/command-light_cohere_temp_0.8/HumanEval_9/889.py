```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of the rolling maximum elements in a given list of integers.
    Args: 
        numbers (List[int]): List of integers
    Returns: 
        List[int]: A list of rolling maximum elements.
    """
    example usage: 
    numbers = [1, 2, 3, 2, 3, 4, 2]
    rolling_max(numbers) 
    -> [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.sort()
    maximum = numbers[0]
    current = numbers[0]
    rolling_maxes = [current]
    for number in numbers[1:]:
        if number > current:
            current = number
        rolling_maxes.append(current)
    current 
    rolling_maxes.append(number)
    rolling_maxes
    return rolling_maxes

```  The function 'rolling_max' takes a list of integers numbers as input and returns a list of the rolling maximum elements in the list. The function first sorts theas list and finds the maximum element in the list, which is set as the initial value for the rolling maximum list. The function then iterates over the list, comparing each element with the current maximum value and updating the rolling maximum list accordingly. The function then returns the maximum value from the rolling maximum list.