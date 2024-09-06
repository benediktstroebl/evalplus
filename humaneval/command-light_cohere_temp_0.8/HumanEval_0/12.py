Here's the Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.3)
   
   0.06, 3.0, 5.0, 5.0, 2.1.5, 0.5, 6, 7, 8.1, 9.0, 10, 1.8, 11, 100, 200]
    """
    The above function has two inputs: a list of numbers and a threshold value. It returns a boolean indicating whether the list contains any two numbers that are closer than each other than the given threshold. 

This function works by comparing each pair of numbers in the list using the `sorted()` function to create a sorted list of numbers, and then using the `distance()` function to calculate the distance between each pair of numbers. The function then checks if the distance is less than the threshold value, the two numbers are considered to be closer than each other.