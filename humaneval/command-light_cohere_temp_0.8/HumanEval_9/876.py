```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function generates a list of rolling maximum elements from a given list of integers.
    It uses the bound method to keep track of the maximum element, 
    which is then appended to the result list.
    """
    list of numbers = numbers
    max_element = numbers[0]
    result = [max_element]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        result.append(max_element)
    return result
    ```