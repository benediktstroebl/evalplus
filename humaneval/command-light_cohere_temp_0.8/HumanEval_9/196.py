```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns a list of the maximum elements
    found while moving over the sequence from left to right
    right.
    Returns a region of numbers, the function first initializes an empty list
    to store the rolling maximum elements. Then, it starts a loop
    moving from left to right and keeps adding the 
    current maximum element to the list until it reaches the first element of the sequence.
    Returns the list containing the maximum elements found in the sequence moving 
    from left to right.
 numbers=[1, 2, 3, 2, 3, 4, 2]
numbers: List[int] = [1, 2, 3, 2, 3, 4, 2]
rolling_max: List[int] = [1, 2, 3, 3, 3, 4, 4]
return rolling_max
```