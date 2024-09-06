```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # type checking for the input parameter and return
    numbers.sort(numbers, key=lambda x: (x, -x)**0.5)
    sort(numbers)
    return numbers[0], numbers[1]
```
This Python function named `find_closest_elements` takes a list of numbers as input and aims to find the closest pairs of elements in the list. It employs the sorting algorithm based on the Euclidean distance to identify pairs of closest elements. The function then returns the `numbers[0]` and `numbers[1]`` as the two closest elements in the list, with the first element being the smaller one.