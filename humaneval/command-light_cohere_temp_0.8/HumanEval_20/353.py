```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort list of numbers in ascending order
    numbers.sort(numbers)
    # find the two elements that are closest to each other
    return (numbers[0], numbers[1])
```
Do you need help with anything else?