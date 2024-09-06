```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), selects and returns two that are the closest to each other and returns them in order (smaller number, larger number).

    Parameters:
    numbers: List[float] - a list of at least two numbers to find the closest pair of.
    Returns:
    pair: Tuple[float, float] - a tuple containing the two numbers in the order of their proximity
    """
    # sort the list using a stable sort method (exclusive or equal comparison between the elements)
    numbers.sort_key(numbers, key=lambda x: x[0])
    first, second = numbers[0], numbers[1]
    return first, second
``` 
This function sorts the list of numbers using the sort_key method with the lambda function as the key parameter. Then, it extracts the two closest numbers from the sorted list and returns them as a tuple.