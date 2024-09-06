Here's the solution:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    https://medium.io/python/25-code/best-match-algorithm.
    # Sort the by the smallest number first
    smaller_num, larger_num = sorted(numbers)
    return smaller_num, larger_num
```