```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from the given list of integers.
    Each element of the
    the list is iterated, and the maximum value of each element
    in the current window is stored.
    In each iteration of the maximum value is updated based on the current element and the 
    maximum value from the previous iteration until the moment is reached.
    >>> nums[-1]
    2
    3
    3
    3
    4
    4
    4
    5
    ...
    """
    rolling_maxes: List[int] = []
    while len(numbers) > 1:
        current_max = numbers[0]
        for num in numbers[1:]:
            current_max = max(current_max, num)
        rolling_maxes.append(current_max)
        numbers.remove(current_max)
    return rolling_maxes

```
This function, rolling_max, takes a list of integers as input and returns a list of the rolling maximum elements found in that list. The rolling maximum is calculated by repeatedly finding the maximum value of each element in the current window and then moving the maximum value to the start of the window, so that it can be calculated efficiently. 

The function works by first initializing an empty list, rolling_maxes, to store the rolling maximum elements. Then, a while loop is used to iterate through the list of numbers, with the loop condition being based on the length of the list. In each iteration, the maximum value of the current element is compared with the maximum value found in the previous iteration, and the larger value is stored in the rolling_maxes list. Finally, the last iteration completes the maximum value is removed from the list of numbers to avoid calculating it again in the next iteration.