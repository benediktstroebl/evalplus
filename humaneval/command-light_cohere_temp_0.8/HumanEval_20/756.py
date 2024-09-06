```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest values
    first_closest, second_closest = (numbers[0] , numbers[1])
    # Sort the list in ascending order of the numbers, and get the first and second elements from the sorted list
    sorted_numbers = sorted(numbers)
    first_closest, second_closest = sorted_numbers[0:1]
    # Return the first and second closest elements in order
    return first_closest, second_closest
```