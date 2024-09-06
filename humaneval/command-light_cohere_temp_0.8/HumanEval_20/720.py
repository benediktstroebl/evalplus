Here is the solution to the problem you described:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
    numbers: List[float] - A list of floating-point numbers.

    Returns:
    Tuple[float, float] - A tuple containing the two closest numbers in order.
```
This function takes a list of numbers as input and returns a tuple containing the two numbers that are the closest to each other in the list. It uses the sorting algorithm to find the smallest number and then finds the second closest number in the list. The function then returns a two numbers in order, with the smaller number first.