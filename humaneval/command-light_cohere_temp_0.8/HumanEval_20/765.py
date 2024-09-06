```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Sort the list in ascending order
    numbers.sort(key=lambda num: num, reverse=True)
    
    # Take the first and second elements from the sorted list
    first, second = numbers[0], numbers[-1]
    
    return first, second
```