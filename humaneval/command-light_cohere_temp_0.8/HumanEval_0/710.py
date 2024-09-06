```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   After has_close_elements([1.0, 8.0, 3.0], 0.2)
    would has_close_elements([1.0, 8.0, 3.0], 0.4))
   l or shift is_list(numbers) function is called with a list of float numbers, and a threshold as the second parameter. The function checks if any two numbers in the list are closer than the threshold. The function returns True if there are any two numbers that are closer than the threshold, and False otherwise.