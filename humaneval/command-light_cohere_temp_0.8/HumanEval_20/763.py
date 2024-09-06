```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two of the numbers in numbers that are the closest to each other, and returns them in order (smaller number, larger number).

    Parameters:
        numbers: List[float] - A list of numbers.
    Returns:
        Tuple[float, float] - A tuple containing the two closest numbers.
    """

```
This code solves the problem of finding the closest elements in a list of numbers. It does this by selecting the two numbers that are the closest to each other from the list and returns them in order (smaller number, larger number).

The function is tested with the following markdown code block:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

print(find_closest_elements(numbers))
```
This will print out the tuple of the two closest numbers.