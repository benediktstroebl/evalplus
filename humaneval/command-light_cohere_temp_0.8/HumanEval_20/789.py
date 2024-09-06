Here's the answer:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    closest = (None, None)
    for i in range(len(numbers)):
        current = numbers[i]
        for j in range(i + 1):
            if current > numbers[j]:
                current = numbers[j]
                if current == closest[0] or closest[1]:
                    closest = (numbers[i], current)
    return closest
```