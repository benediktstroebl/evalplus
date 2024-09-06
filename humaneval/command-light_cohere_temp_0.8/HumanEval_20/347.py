```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda x: x)
    # Get the first and second elements of the sorted list
    first, second = numbers[0], numbers[-1]
    # Return the elements in order (smaller number, larger number)
    return first, second
```