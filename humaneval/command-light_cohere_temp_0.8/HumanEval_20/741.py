Here's a Python script that defines a function `find_closest_elements`, which accepts a list of numbers as an argument and returns a tuple containing the two numbers that are closest to each other:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Find the two closest elements in the list and return them in order (smaller number, larger number).
    
    :return sorted(numbers, key=lambda x: (-x, -abs(x)))[:2]

```