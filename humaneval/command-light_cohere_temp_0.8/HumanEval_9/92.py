```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    A utility function that returns the maximum element found while moving
    iteratively through the list and returns the rolling maximum 
    until the given moment (last element) is reached.
    """
    list of integers is passed in, and the function 
    returns a list of the rolling maximum elements found so far.
    """
 list is returned
    """
    # A simple case
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [max(numbers[:i+1]) for i in range(len(numbers)-1)]
```
The problem of finding the rolling maximum element in a sequence is efficiently solved in this Python code using the max() function and list comprehension.