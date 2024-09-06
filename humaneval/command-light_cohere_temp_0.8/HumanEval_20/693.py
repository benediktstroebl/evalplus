Here is the Python script that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from a supplied list of numbers, and returns them in order of smaller number, larger number.
    """
    list of numbers to function: List[float] numbers

    """
    numbers.sort()
   1, 2, 3, 4, 5

    # Select two elements that are the closest to each other
    # and return them in order (smaller number, larger number)
    smaller_num, larger_num = numbers[0], numbers[1]
    # Swap so smaller number is first
    numbers[0], numbers[1] = numbers[1], numbers[0]
    # Return the two values in order
    return (numbers[0], numbers[1])
```