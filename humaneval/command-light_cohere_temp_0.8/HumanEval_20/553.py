```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Use the first element as a reference
    min_num = min(numbers)
    closest_num = min_num
    i = 0

    # Start with the first number
    for j in range(1, len(numbers)):
        if numbers[j] < min_num:
            closest_num, i = j
        elif numbers[j] > min_num:
            break
        else:
            min_num = numbers[j]

    return i, closest_num
```