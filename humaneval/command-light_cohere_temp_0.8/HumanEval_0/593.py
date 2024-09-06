Here is a Python script that has a self-contained function that checks whether any two elements in the list are closer than a given threshold:
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
```
This function takes two arguments: a List of numbers and a threshold. The function returns True if any two numbers in the list are closer than the threshold. The function uses a difference between the two numbers and checks if it's smaller than the threshold. The function returns False if no such relationship is found.