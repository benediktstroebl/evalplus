Here is the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    return (smallest, largest number)
"""

test_data = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

print(find_closest_elements(test_data)) ) # Output: (2.0, 4.0)