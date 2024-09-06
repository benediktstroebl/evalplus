```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    return any(map(lambda x, y: x<y+threshold or y<x-threshold, numbers))
    ```