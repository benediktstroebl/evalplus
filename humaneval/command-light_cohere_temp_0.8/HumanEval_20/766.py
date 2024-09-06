```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest numbers in the list, in order of their larger values.
    """
    # Initialize variables to store the first and second closest elements
    first, smallest, second = (numbers[0], numbers[1], numbers[2])

    # Sort the list based on the larger values, ensuring the first and second closest elements are at the beginning and end of the sorted list
    numbers = sorted(numbers, key=lambda x: x[1])

    # Use the list comprehension to find the first and second closest elements in the sorted list
    first, smallest, second = numbers[:2]
    return first, smallest, second
```