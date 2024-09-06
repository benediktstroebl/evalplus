```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return the list of rolling maximum elements in the given list of integers.
    Return list contains only therolled maximum elements, in ascending order, 
    until the list is exhausted.
    """
    list of integers is passed as a List[int] 
    argument to the function, and a return list[int] 
    containing the rolling maximum elements is returned.

>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]

>>> rolling_max([5, 6, 7, 8, 9])
[9, 8, 7, 6, 5]

>>> rolling_max([10, 20, 30, 10, 40])
[40, 30, 20, 10, 20]

>>> rolling_max([15, 18, 16, 17, 19, 20])
[19, 18, 17, 16, 15]
```
The function takes a list of integers as input and returns a list of integers containing the rolling maximum elements in the list, in ascending order. The rolling maximum element is calculated by finding the maximum element in the list and then adding one to that maximum element, and repeating the process until the list is exhausted. The function uses the maxima to calculate the maximum element and adds one to it at each iteration to get the rolling maximum.