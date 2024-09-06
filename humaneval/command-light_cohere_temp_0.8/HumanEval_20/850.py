Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two that are the closest to each other and return them in order (smaller number, larger number)"""
    numbers = sorted(numbers, key=lambda x: (x, -x)))
    return numbers[0], numbers[1]
```
The above Python code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers in the list. The code uses the essential sorting key `lambda` function to sort the list of numbers in descending order, and then selects the two closest numbers.