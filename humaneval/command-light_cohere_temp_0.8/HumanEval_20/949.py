Here's the solution:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    # Select two closest elements
    closest1 = min(numbers[0], numbers[1])
    closest2 = max(numbers[0], numbers[1])
    return closest1, closest2
```

This function, named find_closest_elements, takes a list of numbers as input and aims to return the two closest elements from the list, along with their order. The function employs the Python's built-in functions min and max to determine the smallest and largest numbers, respectively. Then, the function returns these two closest numbers and returns them in order (smaller number, larger number).