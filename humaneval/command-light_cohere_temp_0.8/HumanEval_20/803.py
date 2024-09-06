```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two), selects and returns two that are the closest to each other and returns them in order (smaller number, larger number).
    
    Parameters: 
    - numbers: List[float] list of numbers

    Returns: 
    - result: Tuple[float, float] two closest numbers in order of smaller to larger.
    """
    return numbers[0], (numbers[1] - numbers[0])
```