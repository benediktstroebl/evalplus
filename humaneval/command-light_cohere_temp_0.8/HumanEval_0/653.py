```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # using two pointers to compare two elements in the list
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] - numbers[right] < threshold:
            return True
        left += 1
        right -= 1
    return False
``` 
Do you need anything else I can help you with?