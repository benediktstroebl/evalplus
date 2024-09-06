Here is the provided solution:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest elements in the list in order of their magnitude.
    """
    closest_numbers = sorted((x for x in numbers if abs(x - y) <= 1e-10) for y, x in numbers), reverse=True)
    return closest_numbers[0], closest_numbers[1]
```
This function takes a list of numbers as an argument and returns a tuple containing the two closest elements in the list in order of their magnitude. The function uses the to select the two closest elements by comparing each number with every other number in the list and returns the two numbers that are the closest to each other when all the conditions are satisfied.