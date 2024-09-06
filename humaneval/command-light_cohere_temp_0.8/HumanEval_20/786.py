```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest to each other
    first, second = -1, float('inf')
    for i in range(1, len(numbers)):
        if numbers[i] < first:
            first = numbers[i]
        elif numbers[i] > second:
            second = numbers[i]

    # Return the first and second closest to each other
    return (first, second)
```