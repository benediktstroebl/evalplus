```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until the given moment in the sequence.
    """
    List comprehension and rolling window approach is used to achieve this.
    Each number in the list is compared to the maximum element found so far.
    The maximum element is then stored back into the result list
    """
    # initializing list with first element only
    result = [numbers[0]]
    
    # Using list comprehension to find rolling maximum
    for num in numbers[1:]:
        current_max = max(result[-1], num)
        result.append(current_max)
    
    return result
``` 
This function uses a list comprehension and a rolling window approach to efficiently find the maximum element in a sequence. This makes it an concise and easy-to-understand solution that effectively solves the problem.