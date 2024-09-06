```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence."""
    return [n for n, _ in zip(numbers, numbers[1:]) if n > numbers[-1]]
``` 
This code defines a function `rolling_max` that calculates and returns a list of rolling maximum elements in a given input list of integers. It uses the Roll-up average technique to achieve this. 

The function uses the `zip` function to iterate over the input list, and each element is compared with the element from the end of the list using the condition `n > numbers[-1]` to determine the rolling maximum element. 
It then returns a list of these rolling maximum elements.