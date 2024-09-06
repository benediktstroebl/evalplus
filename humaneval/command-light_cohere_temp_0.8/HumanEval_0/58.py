```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the list of numbers, there are any two consecutive elements that are closer than the given threshold.
    Parameters: 
    - numbers: The list of numbers 
    - threshold: The threshold to compare the consecutive elements.
    Returns: 
    - True if there are any two elements in numbers that are closer than threshold, False otherwise.
 """