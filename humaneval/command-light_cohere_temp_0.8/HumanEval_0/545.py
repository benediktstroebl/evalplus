```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 0.0, 0.8]

result = has_close_elements(numbers, 0.8) 
``` 
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns a boolean indicating if any two numbers in the list are closer than the given threshold. The function uses two nested loops to iterate over the list of numbers and checks if the absolute difference between each pair of numbers is less than the given threshold.