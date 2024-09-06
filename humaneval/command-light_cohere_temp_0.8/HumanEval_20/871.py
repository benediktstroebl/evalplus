```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from a supplied list of numbers (of length at least two), and returns them in order (smaller number, larger number).
    # Return the two closest elements in a tuple with their corresponding indices in the original list.
    # Test thea function. It returns the a expected list with the two closest numbers and their respective index positions.
    """
    return sorted(numbers[:2], key=lambda x: (numbers[x], x))
```
The function 'find_closest_elements' accepts a list of numbers as an input parameter and returns a tuple of two numbers that are the closest to each other, as well as their corresponding index positions in the original list. The function sorts the two closest elements in a tuple using the sorted() function, and the key parameter lambda x: (numbers[x], x) ensures that the elements with the smaller and larger values are first in the tuple.