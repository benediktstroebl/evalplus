```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)
    # Define a tuple to store the two closest elements
    closest_pair = tuple(sorted(numbers))[:2])
    # Return the two closest elements in the tuple
    return closest_pair

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
# find_closest_elements(numbers)[:2])
```