```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if x > numbers[-1]]
``` 
This code defines a function `rolling_max` that calculates the rolling maximum element in an array. It uses a important list comprehension to generate a new list containing only the elements greater than the last element in the array. The function returns this list of these rolling maximum elements.