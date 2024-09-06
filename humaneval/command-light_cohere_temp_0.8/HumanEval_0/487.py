```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """ return any two numbers in the list are closer than the threshold."""
    
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 + num2 < threshold:
            return True
    return False

# Example usage
input_numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 2.8, 3.0]
has_close_elements(input_numbers, 0.2)
```