```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in the sequence until a given moment.
    :type numbers List[int] -> List[int]
    """
    numbers = sorted(numbers)
    max_num = numbers[0]
    rolling_maxes = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        rolling_maxes.append(max_num) 
    return rolling_maxes

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
``` 
This function will return a list of the maximum elements after applying the rolling maximum technique on the input list. 

This function is self-contained and can be used to solve the problem for any given list of integers.