Here's the self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two elements in the list are closer than the threshold.
    check(numbers, threshold)
    check = True
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i + 1] < threshold:
            check = False
            break
    return check
```
The script defines a function that takes a list of numbers and a threshold as input and returns a boolean indicating whether any two elements in the list are closer than the threshold. It iterates over the O loop, if two consecutive elements are closer than the threshold, it returns False, otherwise it returns True.