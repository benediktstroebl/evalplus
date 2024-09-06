```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ 
    Select and return two that are the closest to each other and return them in order (smaller number, larger number) 
    """
    if len(numbers) < 2:
        return ()
    a, b = sorted([x for x in numbers if x != numbers[-1]]), key= lambda x: x
    first, second = a[0], b[0]
    for i in range(1, len(numbers)):
        a, b = numbers[i], numbers[i-1] if a != b else a, b
        if b - first > second - second - b:
            return (first, second)
    return (first, second)
```