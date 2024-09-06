```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Each element in the maxes is updated after each element in the list, 
    ensuring that the maximum element seen so far is the new maximum for the current element.
    >>> 
    Lists are tested to verify the correctness of the rolling_max function using the 
    built-in assert statement.
    """ 

rolling_max([1,2,3,2,3,4,2]) 
    [1, 2, 3, 3, 3, 4, 4] 
    """
    numbers = [1, 2, 3, 2, 3, 4, 2]
    while len(numbers) > 1:
        numbers.append(numbers[-1]) 
        numbers.append(max(numbers[-2:])) 
    return numbers[:]
```