```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Return a list of maximum elements, starting from left and moving towards right.
    """
    list is [n for n in numbers if n > max_element]
    """
    max_element = numbers[0]
    for n in numbers[1:]:
        if n > max_element:
            max_element = n
    return [max_element]

# Example function call
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```