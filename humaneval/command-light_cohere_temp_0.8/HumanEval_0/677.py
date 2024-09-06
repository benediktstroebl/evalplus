Here is a self-contained Python script with a function that checks if any two numbers in a given list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return True if any two elements in the list are closer than the threshold; otherwise False
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False
```

This function takes a list of numbers and a threshold as input, and returns True if any two elements in the list are closer than the threshold, otherwise False.

You can use this function with any list of numbers and a threshold to check if any pairs in the list are closer than the threshold.