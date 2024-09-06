```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # use sorted to find the smallest element in the list
    smallest = float('inf')
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest, numbers[0]
```