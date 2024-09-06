```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return all(x != y for x, y in zip(numbers) if abs(x - y) <= threshold)
```
Do you have any other questions regarding Python or coding?