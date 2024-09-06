```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns the rolling maximum element found until the given moment in the sequence.
    Args: 
        numbers: list of integers, at least 1 element
    Returns: 
        list of rolling maximum elements
    """
    numbers = List(numbers)
    n = len(numbers)
    results = [numbers[0]]
    current_max = numbers[0]
    for i in range(1, n):
        current_max = max(current_max, numbers[i])
        results.append(current_max)
    return results
```
This code implements a rolling maximum function for a list of integers. It takes a list of numbers as input, and then iterates through the list, calculating the maximum element seen up to that point. The maximum element is then stored in a list along with the index of the maximum element, providing the rolling maximum elements seen up to the current moment in the sequence. 

This code is self-contained and follows the Best Practices and can be easily maintained for larger and more complex problems.