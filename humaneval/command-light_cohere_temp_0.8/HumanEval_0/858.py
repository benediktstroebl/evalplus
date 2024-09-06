Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    br"""
   +We are floating numbers, but Python is able to compare numbers using the == operator. 
    This function will make sure that it checks for any two numbers in the list that are less than the given threshold. It does this by comparing the minimum and maximum of each pair in the list.