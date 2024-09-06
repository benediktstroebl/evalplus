```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest element
    first, second = numbers[0], numbers[-1]
    # Sort the list based on the criteria
    numbers.sort(numbers, key=lambda x: (x, -abs(x - first)))[0]
    # Return the first and second closest elements
    return first, second
``` 
The function takes a list of numbers and returns a tuple of the first and second closest elements.  The tests the list of numbers to determine the first and second closest elements.