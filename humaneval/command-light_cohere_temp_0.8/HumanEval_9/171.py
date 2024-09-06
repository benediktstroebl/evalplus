```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements in the given list.
    """
    list of numbers is passed to the function as a parameter, 
    and the function returns a list of integers, which are the rolling 
    maximum elements found in the list, starting from the left- index.
    """
    function implements a classic rolling max method using a 
    window of size 3 and a sliding window.
    """return [window_max(numbers[:-1], numbers[1:], numbers[2:], numbers[:-2])
```