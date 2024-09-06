Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.0)
    Dynasty: [float]
    # sort list of numbers in descending order
    numbers.sort(reverse=True)
    # compare two numbers
    if numbers[0] + numbers[1] <= threshold:
        return True
    else:
        return False
    # return has_close_elements(numbers[1:], threshold)
```
The above function takes a list of numbers and a threshold as parameters. It then sorts the for descending order of the numbers in the list. The function returns True if the first two numbers in the list are closer to each other than the threshold. It then compares the other number to the first one, and returns True if the condition is met. It will return False if the condition is not met.