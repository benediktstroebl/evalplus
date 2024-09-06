Here is a self-contained Python script that solves the problem of determining if any two numbers in a given list are closer than a given threshold:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5),False)
   1?)
    return False
    if not any(numbers)
    return True
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]-numbers[j] < threshold:
                return False
    return True
```
This function takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the given threshold. The function first checks if any numbers are empty and returns False. If not, the function iterates over the list, comparing each number with every other number in the list. Finally, if the function returns False, the list does not contain any pairs of numbers that are closer than the given threshold, the function returns True.