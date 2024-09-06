Here's the solution:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    x, y = (min(numbers), max(numbers))
    closest = [x, y]
    for i in range(1, len(numbers)):
        d = (numbers[i] - x) ** 2 + (numbers[i] - y) ** 2
        if d < closest[0]:
            closest = [numbers[i], x]
    return closest[0], closest[1]
```
This script defines a function find_closest_elements that takes a list of numbers as input and returns a tuple of the closest two elements in the list, along with their relative difference.  The other case, the first element in the tuple is the smaller number, and the second element is the larger number. This function uses they selected elements to determine if any other elements are closer to the current closest pair, and updates the closest pair accordingly.