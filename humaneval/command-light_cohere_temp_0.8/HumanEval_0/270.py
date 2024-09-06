```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    for index1, num1 in enumerate(numbers):
        for index2, num2 in enumerate(numbers):
            if abs(num1 - num2) < threshold:
                return True
    return False
```
This code implements a function called has_close_elements, which takes in two arguments: a list of numbers and a threshold value. It uses a loop to compare each number in the list to all other numbers to find if there are any two numbers that are closer than the given threshold.