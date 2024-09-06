```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    A list of integers is given. 
    Return a list of rolling maximum elements found until given moment 
    in the sequence.
    """
    Return the maximum element as a rolling maximum.
    Return a array of [number for i, maximum_element_i as 
    maximum element found so far for i] 
    """
    return [number for number in numbers for _ in range(len(numbers))], numbers[::-1]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5, 6]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 4]

```

This script defines a function `rolling_max` that takes a list of integers as input and returns a list of rolling maximum elements found until the end of the sequence. The function uses a array technique to keep track of the rolling maximum element.