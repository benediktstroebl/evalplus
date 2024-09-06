Here is a self-contained Python function that solves the problem:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # initializing a set to compare two floating numbers
    numbers = set(numbers)
    # checking every two floating numbers, if they are equal or less than the given threshold
    for i in numbers:
        for j in numbers:
            if i == j or j < i <= threshold:
                return True
    return False
```
This function takes in a List of numbers and a threshold as input and returns a Boolean indicating whether any two numbers in the list are closer to each other than the threshold.