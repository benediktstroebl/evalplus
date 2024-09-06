```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Return a list of the rolling maximum elements in the input list.
    """
    First, we initialize a list to store the rolling max elements. Then, we iterate through the array and update the rolling max variable whenever we find a new maximum.
    Return a array with the rolling max elements.
    """
``` 
Here is a self-contained Python function that solves the problem of finding the rolling maximum elements in an array of integers. 

This function takes a list of integers as input and returns a list of integers, where each element is the rolling maximum element found in the input list up to the current moment.