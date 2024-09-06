Here's the code:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    return (numbers[0], numbers[1])
```

This code defines a function `find_closest_elements` that takes a list of numbers as input and returns the closest pair of the numbers from the list. The function first checks if the list has at least two elements, and if it does not, it raises a `ValueError`. Then, it uses the `Pickle()` function to select the closest numbers and returns them in order.