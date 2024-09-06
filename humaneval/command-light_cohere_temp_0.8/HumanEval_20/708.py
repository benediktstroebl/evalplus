```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple of two floats with the first element being the smaller number and the second element being the larger number.
    """
Code Explanation:
    The function `find_closest_elements` takes a list of numbers as input. It then selects the two elements from the list that are closest to each other, and returns them in order, with the first element being the smaller number and the second element being the larger number. This is is used to solve the problem of finding the closest elements in a list.

The `find_closest_elements` function uses the `typing` module to ensure that the input parameter `numbers` is of type `List[float]`. The function then uses a list comprehension to select the two closest elements from the `numbers` list.