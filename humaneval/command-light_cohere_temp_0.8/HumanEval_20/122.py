```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 6, 7]
    first, last = min(numbers[0], numbers[1])
    return (numbers[0], numbers[1])
```

The provided code implements a function called `find_closest_elements`, which accepts a list of floating-point numbers as input. The function identifies two numbers within the list that are closest to each other and returns them as a tuple in ascending order, with the smaller number first. This function employs the`min(numbers[0], numbers[1])` to find the minimum of the first two elements, and then returns the tuple of these two numbers.