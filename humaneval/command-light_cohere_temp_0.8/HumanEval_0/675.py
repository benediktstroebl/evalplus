```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    > numbers[i] <= numbers[j] <= threshold or numbers[j] <= numbers[i] + threshold 
    for i in range(len(numbers)) and j in range(i+1) 
    """
    return True
```