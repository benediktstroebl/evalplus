```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least 2) selects and returns two that are the closest to each other and returns them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - a list of floating-point numbers
    Returns:
        Tuple[float, float] - a tuple containing two of the closest numbers
    """
    numbers.sort()
    smallest_index, largest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[smallest_index]:
            smallest_index = i
        if numbers[i] > numbers[largest_index]:
            largest_index = i
    return numbers[smallest_index], numbers[largest_index]
```
This function takes a list of numbers and returns a tuple of the two closest numbers in the list. The function sorts the numbers and then selects the smallest and largest number, so that the two closest numbers are always returned in order.

The function then returns the two numbers in the tuple, with the smaller number being first and the larger number being second.