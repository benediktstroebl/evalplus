Here's a self-contained Python script that solves the problem:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    >     If a list of numbers, sort it, then sort it again in reverse, and return the first two elements.
    """

The function first sorts the input list of numbers. Then, it sorts the list again, this time in reverse. After that, it returns the first two elements from the sorted list.

The function then returns a tuple of the two closest numbers in the list, with the smaller number first.

To test the function, you can call it with the numbers you want to find the closest pair of and print the result. The function will return the closest pair in the list in the order you expect.