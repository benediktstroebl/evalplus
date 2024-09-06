```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given list.
    """
    - Initialize a maximum element as the first number in the list.
    """
    - Iterate over the range from 1 to the length of the list minus 1
    """
    max_element = numbers[0]
    result = [max_element]  # Initialize with the first element
    for i in range(1, len(numbers)):
        current = numbers[i]
        if current > max_element:
            max_element = current
        result.append(max_element)  # Append the rolling maximum element
    return result
``` 
The function takes a list of integers as input and returns a list of integers that contains the rolling maximum element found up to the given moment in the sequence.

You can use this function to solve the problem and pass the test.