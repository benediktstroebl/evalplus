```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return the rolling maximum element found until the given moment
    in the sequence.
    Parameters:
    numbers (List[int]): Input list of integers.
    Returns:
    list of rolling maximum elements.
    """

Return:
    list of integers, where the rolling maximum element is placed.
    """
    numbers.max = max(numbers)
    rolling_max = [numbers[i] for i in range(len(numbers))]
    rolling_max.append(numbers[i] if numbers[i] > rolling_max[i])
    return rolling_max

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
The above Python code snippet presents a function named `rolling_max`, designed to generate a list of rolling maximum elements within a given sequence of integers. It uses the maximum element detection and lists manipulation to achieve this. The function operates by accepting an list of integers as input and returning a new list where the rolling maximum element is positioned at the end. 

The example usage demonstrates how the function can be invoked with a list of integers, and the resulting list of rolling maximum elements is then printed.