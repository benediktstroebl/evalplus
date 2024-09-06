```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements.
    The list of rolling max elements, starting from any index and moving to the end of the list.
    each element in the list will be the rolling maximum found so far,
    rolling max is calculated by looking at the previous index and taking max of the current and
    previous elements.
    """
    list of rolling max elements.
    """ List[ return a a list of rolling max elements found until the end of the list."""

# Example:
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_res = rolling_max(numbers)
print("Rolling Max Elements:", rolling_max_res)
```
The provided code defines a function called rolling_max that takes a list of integers as input and generates a new list of rolling maximum elements. The rolling_max function uses the approach to calculate the rolling maximum element by considering both the current element and the previous element in the list. This new list of rolling maximum elements is then returned and displayed.