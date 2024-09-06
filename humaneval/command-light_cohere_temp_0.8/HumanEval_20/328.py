Here is a self-contained Python script that solves the problem of finding the closest elements from a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
        numbers: List[float]

    Returns:
        Tuple[float, float]: The two closest elements.
 """
    Returns:
        return numbers[0] if numbers[0] < numbers[1] else numbers[1]
    """

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    open_numbers, numbers = List(range(1, 6))
    result = find_closest_elements(numbers)
    assert result == (2.0, 4.0)  # This2.0, 4.0)  #
2.0, 4.0)  #
more tests can be added to test the correctness of the function.