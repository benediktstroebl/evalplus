```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    Each element in the max is calculated and stored until the next maximum is found.
    """
    list of numbers -> list of integers that contain the rolling max elements. 
    """
   
    rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = List(numbers)
    max_rolling = List()
    current_max = None
    for num in numbers:
        if current_max is None or num > current_max:
            current_max = num
        elif num == current_max:
            max_rolling.append(current_max)
            current_max = None
    max_rolling.append(num)
    return max_rolling
``` 
This function will take a list of integers and return a new list that contains the rolling maximum elements in order.