```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    top = min(numbers)
    for i in range(len(numbers)-1):
        if numbers[i] > top:
            top = numbers[i]
    return Tuple(top, numbers[0])
```