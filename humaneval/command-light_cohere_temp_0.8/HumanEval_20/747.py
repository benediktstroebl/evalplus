```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort numbers based on value
    numbers.sort(numbers, reverse=True)
    # sort them based on index (for stability)
    numbers.sort(numbers, reverse=False)
    # select the first two elements of the sorted list
    return Tuple(numbers[0], numbers[1])
```
This code will return a tuple with the two closest elements of the list, in order of decreasing values.