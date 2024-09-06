```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Finds the two closest elements in the list and returns them in order.

    Parameters:
    List[float] numbers: list of numbers.
    """
    tuple (closest_smaller_number, closest_larger_number) is returned, where
    closest_smaller_number is the smaller number in the list, and closest_larger_number is the larger number in the list.
    """return find_closest_elements([1.0, 2.0, 3.0, 4.0, 5])
```

is a function that takes a list of numbers as an argument. It returns a tuple that contains the two closest elements to each other in the list. This is done by selecting the smallest and largest number, respectively, from the list and then returning them in order.