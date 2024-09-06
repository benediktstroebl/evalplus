```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    ## Returns: boolean indicating if any two elements are closer than threshold """
    return any(map(lambda x, y: x<threshold and y<threshold,numbers))
```
Do you need anything else to complete this request?