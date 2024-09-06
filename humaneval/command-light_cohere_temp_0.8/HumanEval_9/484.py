```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num != 0]  # Filter out zero values
    max_index = numbers.max()  #index to keep the maximum element
    return [max(numbers[max_index:])]
```