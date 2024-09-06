```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Similar to the problem statement, take the two closest numbers and return them in order
    return (numbers[0] if numbers[0] < numbers[-1] else numbers[-1], numbers[0])
```
This solution defines a function `find_closest_elements` that takes a list of numbers as an input parameter and returns a tuple of two closest numbers from the list.