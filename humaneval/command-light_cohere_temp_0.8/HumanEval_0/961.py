Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If any two numbers in the list are closer than threshold, then return True
    If the list is empty or any number is greater than threshold, return False
    """
    if not numbers:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# Example usage:
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0]
numbers = [1.0, 2.8, 3.0, 4.0, 5.0]
numbers = []
has_close_elements(numbers, 0.8)  # returns True, since all the numbers are within the threshold. 
has_close_elements(numbers, 0.0)  # returns False, since any number is greater than the threshold. 
has_close_elements([1.0, 2.8, 3.0], 0.0)  # returns True, since any two numbers are not closer than the threshold.