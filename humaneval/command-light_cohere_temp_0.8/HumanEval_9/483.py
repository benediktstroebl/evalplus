```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    """
    first, the maximum element in the list, and then keep recomputing the maximum element and adding it to the result until the list is updated with the next element. 
    Returns a max(numbers)
    """
    # Initialize the list with the first element of the sequence as the maximum
    result = [numbers[0]]
    
    # Move through the list and update the result with the maximum element of the current sublist
    while numbers:
        current_max = numbers[0]
        for num in numbers[1:]:
            if num > current_max:
                current_max = num
        result.append(current_max)
        numbers.append(num)
    
    return(result)
```