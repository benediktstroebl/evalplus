```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Find two closest elements and return them in order.
    """
    return (sorted((numbers[0] if i < len(numbers) - 1 else numbers[i]) for i in range(len(numbers) - 1)), key=lambda x: x[1] - x[0])[0])
```