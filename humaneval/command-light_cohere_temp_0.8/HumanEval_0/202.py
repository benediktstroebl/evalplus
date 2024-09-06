```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x <= y for x, y in zip(numbers, numbers[1:])) and numbers[1:] <= threshold
```
Do you have any other questions related to Python or other topics that you would like me to help with?