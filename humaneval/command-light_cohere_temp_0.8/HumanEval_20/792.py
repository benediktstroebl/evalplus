```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize two elements of the list as the closest to each other.
    closest1, closest2 = (min(numbers), max(numbers))
    
    # Sort the list based on the comparison of elements
    numbers.sort(key=lambda n: -n)
    
    # Return the first two elements of the sorted list
    return next(numbers[0:2], (closest, closest2))

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result)
```