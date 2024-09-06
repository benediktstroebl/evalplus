```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a list of integers.
    The sequence is [1, 2, 3, 2, 3, 4, 2]
    return [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [x for x in numbers if x != 0]  # Remove zero values
    return [max(numbers[i:], numbers[i+1 :]) for i in range(len(numbers) // 2)]
```