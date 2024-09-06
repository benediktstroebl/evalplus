Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
```
The code provides a function called `has_close_elements` that checks if any two numbers in the list are closer than a given threshold. The function uses two nested loops and the absolute difference between the numbers to check if it's smaller than the threshold.