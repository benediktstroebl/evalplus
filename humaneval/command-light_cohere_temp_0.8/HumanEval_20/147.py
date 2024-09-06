Here is a Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)"""
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda x: x)
    # Get the two closest numbers from the sorted list
    first = next((x for x in numbers if x < numbers[-1]), last = next((x for x in numbers if x > numbers[0]))
    # Return the two closest numbers in order
    return first, last
```
This function takes a list of numbers as input and returns a tuple of two floats: the first is the smaller of the two numbers and the second is the larger of the two numbers. 
This function will sort the list of numbers in ascending order and then will return the two closest numbers in the list.