```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    L = len(numbers)
    numbers.sort(::-1)
    i = L // 2
    while i >= 0 and numbers[i] > numbers[(i + 1) % L]:
        numbers[i], numbers[i + 1] = numbers[(i + 1) % L], numbers[i]
        i -= 1
    return numbers[0], numbers[1]
```