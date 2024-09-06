```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False

# Example usage
numbers = [1.0, 2.8, 3.0, 4.8, 5.0, 0.0, 6.0]
has_close_elements(numbers, 0.0)
``` 
This script defines a function `has_close_elements` that checks whether any two consecutive elements in the given list are closer than a given threshold. The function returns True if any of the conditions is met, otherwise it returns False.