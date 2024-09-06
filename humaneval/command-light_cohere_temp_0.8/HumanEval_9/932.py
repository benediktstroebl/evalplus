```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    This function takes a list of integers and returns the list of rolling maximum elements found until the given moment in the sequence.
    """
    list of numbers is passed as a parameter 
    and returns a list of rolling maximum elements found until the given moment. 
    The maximum element of the sequence is defined as the maximum 
    of the current element and the previous maximum element. 
    
    Test cases:
    - Test with a list of integers: [1, 2, 3, 4, 5]
    - Test with a empty list: []
    - Test with negative numbers: [-2, -4, -6]
    """
    numbers = List[int](numbers)
    result = [num for num in numbers]
    while len(result) > 1:
        current_max = max(result[-1], result[-2])
        result[0], result[-1] = current_max, result[-2]
    return result
``` 
The function is designed to take a list of integers and generate a list of the rolling maximum elements found until a given moment in the sequence. The algorithm maintains the maximum element of the sequence, and whenever the length of the sequence is greater than two, the maximum of the current element and the previous maximum element. 

This is the way it simulates the rolling effect of maximum elements.