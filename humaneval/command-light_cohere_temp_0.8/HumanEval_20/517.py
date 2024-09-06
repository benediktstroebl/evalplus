```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Check for length at least 2
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    # Sort the list of numbers
    numbers.sort(numbers)
    # Get the two numbers that are closest to each other and return them in order (smaller number, larger number)
    result = (numbers[0], numbers[-1])
    return result
```