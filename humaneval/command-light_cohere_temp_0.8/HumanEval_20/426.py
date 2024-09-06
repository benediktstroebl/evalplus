```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Selecting the two closest elements and returning them in order of smaller number, larger number.
    smaller, float = min(numbers[0], numbers[1])
    closest = (numbers[0], numbers[1])
    return smaller, closest
```

This solution uses the min() function to compare the two elements of the list and returns the smallest number first, which is the closest to the second element. The function then returns the result as a tuple containing both values.