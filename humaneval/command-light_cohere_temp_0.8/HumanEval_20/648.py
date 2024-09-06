Here's a solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return numbers, 0.0, 1.2
    else:
        a, closest = min(numbers[0], numbers[1])
        b, closest = find_closest_elements(numbers[1:])
        return a, b
```
This function takes a list of numbers and returns a tuple of the two numbers that are closest to each other. The function works by using a nested function to find the two closest numbers and then returns them in order (smaller number, larger number).