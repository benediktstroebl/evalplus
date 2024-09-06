```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Returns the two closest elements from a supplied list of numbers and returns them in order (smaller number, larger number)
    """
    if len(numbers) < 2:
        return numbers
    a, b = (numbers[::2], numbers[1::2])
    # sort in descending order
    for i in range(len(numbers)):
        if numbers[i] > a[0]:
            a, b = b, a
        elif numbers[i] < a[0]:
            break
    return a[0], a[1]
```