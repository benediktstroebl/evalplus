Here's a self-contained Python script with a function that solves the problem of finding the closest elements from a list of numbers:

```python
from typing import List
from typing import Tuple
def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements that are the closest to each other and returns them in order (smaller number, larger number).
    The function assumes that the input list has at least two elements."""
    # Sort the list
    sorted_numbers = sorted(numbers)
    # Select the two closest elements
    first_element = sorted_numbers[0]
    second_element = sorted_numbers[1]
    return (first_element, second_element)
```

This code defines a function called `find_closest_elements`, which takes a list of numbers as an input and returns a tuple of the two closest elements in the list. The function sorts the by the list of numbers and then selects the two closest elements, which are the first and second elements of the list.