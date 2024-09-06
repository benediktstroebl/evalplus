```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements from a given list of integers.
    The rolling max elements will be the maximum element found until the moment m, 
    where the list length becomes m.
    Return a list of rolling max elements for each moment.
    """
Return: a list of lists, each containing rolling max elements at corresponding moments.
    """Example: [1, 2, 3, 3, 3, 4, 4]
    """
    max_elements = []
    for i in range(len(numbers)):
        # find the maximum element until moment i
        max_element = numbers[i]
        moment = i
        while moment < len(numbers) and numbers[moment] > max_element:
            max_element = numbers[moment]
            moment += 1
        max_elements.append([max_element])
    return max_elements
```