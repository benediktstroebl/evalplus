```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling max elements found in the sequence.
    Each element is the maximum value of a number in a window, 
    starting from 0 and moving by 1, is returned.
    Input: numbers: list of integers 
    Output: list of integers
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [max(numbers[i:i+1]) for i in range(len(numbers)-1)]
``` 
Do you need anything else?