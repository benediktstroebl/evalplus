```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    Args:
        numbers (List[int]): The list of integers
    Returns:
        List[int]: A list of rolling maximum elements.
    """
    generates a list of rolling maximum elements, the rolling maximum of a
        given number is the maximum value among the previous numbers.
    """
    returns a list of integers, where the ith element is the rolling maximum of 
        the elements before it in the list.
    """
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max = [max(x, numbers[-1]) for x in numbers]
print(rolling_max)  # [1, 2, 3, 3, 3, 4, 4]
```