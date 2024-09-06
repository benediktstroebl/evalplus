```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list of integers.
    Input: numbers - list of integers
    Output: list of rolling maximum elements found until the moment of the sequence.
    """
    initial rolling max is 1 
    """
    rolling_max_element = 1
    current_number = numbers[0]

    result = [rolling_max_element]
    for number in numbers[1:]:
        current_number = max(current_number, number)
        rolling_max_element = current_number
    result.append(rolling_max_element)
    return result

# Unit tests
numbers = [1, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
``` 
This function uses a simple strategy where it maintains the rolling max element and updates it whenever a larger element is encountered. It starts with the initial rolling max element as 1 and keeps appending this rolling max element to the result list.