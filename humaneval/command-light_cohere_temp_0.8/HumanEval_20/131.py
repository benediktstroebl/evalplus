```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import Tuple
    numbers = sorted(numbers)
    a, b = zip(numbers, numbers[1:])
    return (min(a), max(b)) if len(numbers) > 1 else (numbers[0], numbers[1]))
```