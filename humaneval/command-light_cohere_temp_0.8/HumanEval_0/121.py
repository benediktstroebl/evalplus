Here is a self-contained Python script with a function that solves the problem of checking if any two numbers in a list are closer than a given threshold:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    Returns true if any two numbers in the list are closer than the threshold, otherwise, returns false.
    """ if any elements of numbers in the list are the same, it will return false since the numbers are not closer than the threshold. Then it iterates through the it list to find the smallest and largest elements, and checks if the difference between the two is less than the threshold. The code then loops through the smallest element and compares it to each number in the list until it finds the largest one, if any number in the list is greater than the largest one, it will return false. Otherwise, it will return true.