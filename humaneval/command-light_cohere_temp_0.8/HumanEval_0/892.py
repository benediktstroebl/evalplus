```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If there are two numbers in the list with a difference less than or equal to the given threshold, return True
    If no such pair exists, return False
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This function uses a nested loop to compare all possible pairs of numbers in the list, it returns True if there are two numbers in the list that have a difference less than or equal to the given threshold.