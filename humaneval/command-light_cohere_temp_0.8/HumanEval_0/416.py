```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return True if any set of two consecutive elements in numbers list are closer than threshold, else False
    """
    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```

This code implements a function called `has_close_elements` which checks if any two consecutive elements in a list of numbers are closer than a given threshold.  The function uses two nested for loops to iterate over the list of numbers and checks if the difference between the two consecutive elements is less than or equal to the threshold.