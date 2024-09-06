Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :param numbers: List[float] - list of numbers
    :param threshold: float - threshold to check
    :return: bool - True if any two numbers in the list are closer than the threshold, else False
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```

This script defines a function called `has_close_elements` that takes in two arguments: a list of numbers and a threshold value. The function loops through two nested loops and compares each number in the list to the next number, and if the difference between the two numbers is less than the threshold, then it returns True.  The function will return a boolean value that indicates whether any two numbers in the list are closer than each other.