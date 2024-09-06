Here's the code:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This code defines a function `has_close_elements` that checks whether any two numbers in a given list are closer to each other than a given threshold. The function iterates over the the two keys of a list of numbers, and checks if the difference between these two numbers is less than or equal to the threshold. If the condition is met, it returns `True`. Otherwise, it returns `False`.