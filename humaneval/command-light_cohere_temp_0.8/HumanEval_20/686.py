Here is the self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Return the two closest numbers and the order of the first element in the list.
    numbers.sort()  # least elements element in sorted order, i.
    # The list comprehension is often used to sort lists in Python.
    return (numbers[0], numbers[1])
```