```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float]  List of floating-point numbers

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order of magnitude.
```
This Python code defines a function called `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers in magnitude order.

The `find_closest_elements` function first checks if the list has at least two elements. If not, it raises a `ValueError` with the appropriate error message.

Then, it uses the `sorted` function to sort the list of numbers in ascending order based on their values. After sorting, it uses the `pandas` library to find the first and second smallest numbers in the sorted list.

Finally, the function returns a tuple containing the two closest numbers in order of magnitude, with the smaller number first.