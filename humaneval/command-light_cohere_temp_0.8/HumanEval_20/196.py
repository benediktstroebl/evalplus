```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # check if length of the list is not 2
    if len(numbers) != 2:
        raise ValueError("Input list must contain exactly two numbers")

    # sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # get the first and second elements in the sorted list
    first = sorted_numbers[0]
    second = sorted_numbers[1]

    return first, second
```