```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers (List[float]): list of floating-point numbers

    Returns:
        Tuple[float, float]: a tuple containing the two closest numbers in the list, with the smaller number first.
    """
code

def test_find_closest_elements(numbers):
    # Test the function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8]

    numbers.list(numbers)

    assert find_closest_elements(numbers) == (1.0, 5.0))  #

    assert find_closest_elements(numbers) == (5.0, 1.0))  #
assert find_closest_elements(numbers) == (2.0, 3.0))
assert find_closest_elements(numbers) == (4.0, 2.0))
```