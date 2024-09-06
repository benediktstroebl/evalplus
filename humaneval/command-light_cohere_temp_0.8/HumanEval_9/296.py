```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found in the given sequence.
    """
    list of numbers to be passed as the parameter
    """
    numbers = List(sorted(numbers))
    return [x for x in numbers if x == numbers[-1]]
``` 
The above function uses list comprehension and the sorted function to solve the problem. It then uses the most efficient way to return the rolling maximum element found in the list of numbers.